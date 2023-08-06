#from itertools import product
#import itertools
import random
from wammodels.descomp import Descomp
import pandas as pd

class Combination:
	def __init__(self,range_list):
		self.range_list = range_list
		self.list_comb = self.create_combination()
		self.descomp = Descomp()
		self.list_comb_save = []

	def create_combination(self):
		combinations = {}
		for key,i in enumerate(self.range_list):
			combinations[key]   =   []
			coef = ""

			if len(i) > 1:
				settings_var    =   i[1]
				lag = 0
				

				if "coef" in settings_var:
					coef = settings_var["coef"][0]

				if "adstock_rate" in settings_var:
					adstock_rate   =  settings_var["adstock_rate"]
					min = int(adstock_rate[0]*100)
					if len(adstock_rate) > 1:
						max = int(adstock_rate[1]*100)
						freq = int(adstock_rate[2]*100)
					else:
						max = min+1
						freq = min
					for range_adstock_rate in range(min,max+1,freq):
						range_adstock_rate = range_adstock_rate/100.0
						if "v" in settings_var:
							v   =   settings_var["v"]
							min_v = int(v[0]*100)
							if len(v) > 1:
								max_v = int(v[1]*100)
								freq_v = int(v[2]*100)
							else:
								max_v = min_v+1
								freq_v = min_v
							for range_v in range(min_v,max_v+1,freq_v):
								range_v = range_v/100.0
								if "rho" in settings_var:
									rho  =  settings_var["rho"]
									min_rho = int(rho[0]*100)
									
									if len(rho) > 1:
										max_rho = int(rho[1]*100)
										freq_rho = int(rho[2]*100)
									else:
										max_rho = min_rho+1
										freq_rho = min_rho
									for range_rho in range(min_rho,max_rho+1,freq_rho):
										range_rho = range_rho/100.0

										if "lag" in settings_var:
											lag = settings_var["lag"]
											min_lag = int(lag[0])
											if len(lag) > 1:
												max_lag = int(lag[1])
												freq_lag = int(lag[2])
											else:
												max_lag = min_lag+1
												freq_lag = min_lag

											for range_lag in range(min_lag,max_lag+1,freq_lag):
												dict_adstrock_rage = dict([("adstock_rate",range_adstock_rate),("v",range_v),("rho",range_rho),("lag",range_lag),("coef",coef)])
												combinations[key].append([i[0],dict_adstrock_rage])
										else:
											dict_adstrock_rage = dict([("adstock_rate",range_adstock_rate),("v",range_v),("rho",range_rho),("lag",lag),("coef",coef)])
											combinations[key].append([i[0],dict_adstrock_rage])
						else:
							if "lag" in settings_var:
								lag = settings_var["lag"]
								min_lag = int(lag[0])
								if len(lag) > 1:
									max_lag = int(lag[1])
									freq_lag = int(lag[2])
								else:
									max_lag = min_lag+1
									freq_lag = min_lag

								for range_lag in range(min_lag,max_lag+1,freq_lag):
									dict_adstrock_rage = dict([("adstock_rate",range_adstock_rate),("lag",range_lag),("coef",coef)])
									combinations[key].append([i[0],dict_adstrock_rage])
							else:
								dict_adstrock_rage = dict([("adstock_rate",range_adstock_rate),("lag",lag),("coef",coef)])
								combinations[key].append([i[0],dict_adstrock_rage])
										
				elif "diff" in settings_var:
					diff  =  settings_var["diff"]
					min_diff = int(diff[0])
					if len(diff) > 1:
						max_diff = int(diff[1])
						freq_diff = int(diff[2])
					else:
						max_diff = min_diff+1
						freq_diff = min_diff
					for range_diff in range(min_diff,max_diff+1,freq_diff):
						dict_diff_rage = dict([("diff",range_diff),("lag",lag),("coef",coef)])
						combinations[key].append([i[0],dict_diff_rage])
				else:
					if "lag" in settings_var:
						lag = settings_var["lag"]
						min_lag = int(lag[0])
						if len(lag) > 1:
							max_lag = int(lag[1])
							freq_lag = int(lag[2])
						else:
							max_lag = min_lag+1
							freq_lag = min_lag

						for range_lag in range(min_lag,max_lag+1,freq_lag):
							dict_lag_rage = dict([("lag",range_lag),("coef",coef)])
							combinations[key].append([i[0],dict_lag_rage])
					else:
						dict_lag_rage = dict([("coef",coef)])
						combinations[key].append([i[0],dict_lag_rage])
			else:
				combinations[key].append([i[0]])
		
		#variable = list(combinations.values())
		#combined_list = list(product(*variable))
		return combinations

	def get_combination_list(self):
		return self.list_comb

	def get_combination_group(self):
		variable = list(self.list_comb.values())
		combined_list = list(product(*variable))
		return combined_list

	def search_combinations(self,max_comb=1,pvalor=0.11,show_count_comb=True):
		self.list_comb_save = []

		while len(self.list_comb_save) < max_comb:
			comb_random = self.get_combination_rand()
			(get_var_prepare) = self.descomp.prepare_var(comb_random)
			(df,formula) = self.descomp.create_df_formula(*get_var_prepare)
			(EQ1,X_Model) = self.descomp.create_model(formula,df)
			p_valor =  EQ1.pvalues.lt(pvalor).sum()
			if (len(EQ1.pvalues) == p_valor):
				coef_get   	=  [i[1]["coef"] if len(i) > 1 and "coef" in i[1] else "" for i in get_var_prepare]
				if self.get_check_coef(coef_get,EQ1.params):
					one_v   	=  [i[1]["adstock_rate"] if len(i) > 1 and "adstock_rate" in i[1] else 0 for i in get_var_prepare]
					v_v     	=  [i[1]["v"] if len(i) > 1 and "v" in i[1] else 0 for i in get_var_prepare]
					rho_v   	=  [i[1]["rho"] if len(i) > 1 and "rho" in i[1] else 0 for i in get_var_prepare]
					diff    	=  [i[1]["diff"] if len(i) > 1 and "diff" in i[1] else 0 for i in get_var_prepare]
					lag    		=  [i[1]["lag"] if len(i) > 1 and "lag" in i[1] else 0 for i in get_var_prepare]
								
					self.list_comb_save.append([EQ1,X_Model,[one_v,v_v,rho_v,diff,lag,coef_get]])
					if show_count_comb:
						print("Combinations found successfully {} ~ {}".format(len(self.list_comb_save),max_comb))
			if len(self.list_comb_save) >= max_comb:
				break
		if not show_count_comb:		
			print("Combinations found.")

		#return self.list_comb_save

	def get_check_coef(self,coef_get,coef):
		count_total_coef = 0
		for count,value in enumerate(coef_get):
			if value != "":
				if value == "+" and coef[count] > 0:
					count_total_coef += 1
				elif value == "-" and coef[count] <0:
					count_total_coef +=1
		non_empty_values = [val for val in coef_get if val != '']
		count32 = len(non_empty_values)
		if count32 == count_total_coef:
			return True

		return False
	def get_descomp(self):
		return self.descomp

	def get_size_comb(self):
		return len(self.list_comb_save)

	def get_eq1_comb(self,index):
		if index >= len(self.list_comb_save):
			return "Error max lenght list : {} max".format(len(self.list_comb_save))
		return self.list_comb_save[index][0]

	def get_df_comb(self,index):
		if index >= len(self.list_comb_save):
			return "Error max lenght list : {} max".format(len(self.list_comb_save))
		return self.list_comb_save[index][1]

	def get_var_comb(self,index,format_v="dataframe"):
		if index >= len(self.list_comb_save):
			return "Error max lenght list : {} max".format(len(self.list_comb_save))

		if "dataframe" in format_v:
			df = pd.DataFrame(self.list_comb_save[index][2]).T
			df.columns = ["adstock_rate","v","rho","diff","lag","coef_restric"]
			return df

		return self.list_comb_save[index][2]

	def get_var_cp(self,index):
		if index >= len(self.list_comb_save):
			return "Error max lenght list : {} max".format(len(self.list_comb_save))

		coef_get = self.list_comb_save[index][0].params
		p_value_get = self.list_comb_save[index][0].pvalues

		p_value_formatted = [format(x, '.7f') for x in p_value_get]
		df = pd.DataFrame([coef_get.values,p_value_formatted]).T
		df.columns = ["coef","pvalor"]
		return df

	def get_var_all(self,index):
		if index >= len(self.list_comb_save):
			return "Error max lenght list : {} max".format(len(self.list_comb_save))

		var_df = self.get_var_comb(index)
		df_cp =  self.get_var_cp(index)

		df_final = pd.concat([var_df,df_cp],axis=1)
		return df_final

	def get_combination_rand(self):
		comb_send = []
		prueba =  []

		for i in range(0,len(self.list_comb)):
			number = random.randint(0, len(self.list_comb[i])-1)
			comb_send.append(self.list_comb[i][number])

		return comb_send