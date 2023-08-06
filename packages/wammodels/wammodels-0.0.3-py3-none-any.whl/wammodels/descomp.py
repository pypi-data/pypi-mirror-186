import wammodels.global_func as gf
import pandas as pd
import numpy as np
import statsmodels.api as sm
from patsy import dmatrices

class Descomp:
	def __init__(self):
		pass

	def prepare_var(self,list_var):
		list_var_edit = []
		
		for index,value in enumerate(list_var):
			data_info =  list_var[index][0]
			if len(list_var[index]) > 1:
				keys_extra = list_var[index][1]
			
				adstock_rate = 0
				v = 0
				rho = 0
				lag = 0
				coef = ""

				if "lag" in keys_extra:
					lag = keys_extra["lag"]

				if "coef" in keys_extra:
					coef = keys_extra["coef"]

				if "adstock_rate" in keys_extra:
					adstock_rate = keys_extra["adstock_rate"]
					if "rho" in keys_extra:
						rho = keys_extra["rho"]
						if "v" in keys_extra:
							v = keys_extra["v"]
							list_var_edit.append([gf.stockbudg(data_info,adstock_rate = adstock_rate, rho=rho, v=v),{"adstock_rate":adstock_rate,"rho":rho,"v":v,"lag":lag,"coef":coef}])
						else:
							list_var_edit.append([gf.stockbudg(data_info,adstock_rate = adstock_rate, rho=rho),{"adstock_rate":adstock_rate,"rho":rho,"v":v,"lag":lag,"coef":coef}])
					else:
						list_var_edit.append([gf.adstock(data_info,adstock_rate = adstock_rate),{"adstock_rate":adstock_rate,"rho":rho,"v":v,"lag":lag,"coef":coef}])
							
				elif "diff" in keys_extra:
					diff_index = keys_extra["diff"]
					list_var_edit.append([data_info.diff(diff_index),{"diff":diff_index,"lag":lag,"coef":coef}])

				else:
					list_var_edit.append([data_info,{"lag":lag,"coef":coef}])

			else:
				list_var_edit.append([data_info])
		
		return list_var_edit

	def prepare_formula(self,list_var):
		get_var_prepare = self.prepare_var(list_var)
		get_var_prepare_only = [x[0] for x in get_var_prepare]
		return get_var_prepare_only

	def new_formula(self,formula_get,get_var_prepare):
		v_lag   =  [i[1]["lag"] if len(i) > 1 and "lag" in i[1] else 0 for i in get_var_prepare]
		formula_array =  formula_get.replace("+","").replace("~","").split()
		new_formula = ""
		for key,valor in enumerate(v_lag):
			if key == 1:
				new_formula += " ~ "
			if key > 1:
				new_formula += " + "
			if valor != 0:
				formula_array[key] = f"{formula_array[key]}.shift({valor})"
			new_formula += formula_array[key]
		return new_formula

	def create_df_formula(self,*args):
		args_v = [x[0] for x in args]
		dfs = [pd.DataFrame(arg) if isinstance(arg, np.ndarray) else pd.DataFrame(arg) if isinstance(arg, list) else pd.DataFrame(arg) for arg in args_v]
		df = pd.concat(dfs, axis=1)
		df.columns = ['v' + str(i) for i in range(1, len(df.columns)+1)]
		df = df.sort_index()
		formula = df.columns[0] + " ~ " + " + ".join(df.columns[1:])
		formula_new = self.new_formula(formula,args)
		return df, formula_new

	def create_model(self,formula,df):
		y_model, x_model = dmatrices(formula, data=df, return_type='dataframe')
		result = sm.OLS(y_model, x_model).fit()
		return (result,x_model)

