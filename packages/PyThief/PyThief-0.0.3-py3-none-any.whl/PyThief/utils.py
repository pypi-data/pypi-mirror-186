# -*- coding: utf-8 -*-
import numpy as np


class Utilities:
    
    def __init__(self):
        pass
    
    def build_smatrix(self,annual_agg,semiannual_agg,fourmonth_agg,threemonth_agg):
        if annual_agg:
            s_matrix = np.ones((12,),dtype=int)
            s_matrix = np.atleast_2d(s_matrix)
            s_matrix = np.concatenate((s_matrix,[[1,1,1,1,1,1,0,0,0,0,0,0]]))
            s_matrix = np.append(s_matrix, [[0,0,0,0,0,0,1,1,1,1,1,1]],axis = 0)
            s_matrix = np.append(s_matrix, [[1,1,1,1,0,0,0,0,0,0,0,0]],axis = 0)
            s_matrix = np.append(s_matrix, [[0,0,0,0,1,1,1,1,0,0,0,0]],axis = 0)
            s_matrix = np.append(s_matrix, [[0,0,0,0,0,0,0,0,1,1,1,1]],axis = 0)
            s_matrix = np.append(s_matrix, [[1,1,1,0,0,0,0,0,0,0,0,0]],axis = 0)
            s_matrix = np.append(s_matrix, [[0,0,0,1,1,1,0,0,0,0,0,0]],axis = 0)
            s_matrix = np.append(s_matrix, [[0,0,0,0,0,0,1,1,1,0,0,0]],axis = 0)
            s_matrix = np.append(s_matrix, [[0,0,0,0,0,0,0,0,0,1,1,1]],axis = 0)
            s_matrix = np.append(s_matrix, [[1,1,0,0,0,0,0,0,0,0,0,0]],axis = 0)
            s_matrix = np.append(s_matrix, [[0,0,1,1,0,0,0,0,0,0,0,0]],axis = 0)
            s_matrix = np.append(s_matrix, [[0,0,0,0,1,1,0,0,0,0,0,0]],axis = 0)
            s_matrix = np.append(s_matrix, [[0,0,0,0,0,0,1,1,0,0,0,0]],axis = 0)
            s_matrix = np.append(s_matrix, [[0,0,0,0,0,0,0,0,1,1,0,0]],axis = 0)
            s_matrix = np.append(s_matrix, [[0,0,0,0,0,0,0,0,0,0,1,1]],axis = 0)
            s_matrix = np.concatenate((s_matrix,np.eye(12)))
        elif semiannual_agg:
            s_matrix = np.ones((6,),dtype=int)
            s_matrix = np.atleast_2d(s_matrix)
            s_matrix = np.concatenate((s_matrix,[[1,1,1,0,0,0]]))
            s_matrix = np.append(s_matrix, [[0,0,0,1,1,1]],axis = 0)
            s_matrix = np.append(s_matrix, [[1,1,0,0,0,0]],axis = 0)
            s_matrix = np.append(s_matrix, [[0,0,1,1,0,0]],axis = 0)
            s_matrix = np.append(s_matrix, [[0,0,0,0,1,1]],axis = 0)
            s_matrix = np.concatenate((s_matrix,np.eye(6)))
        elif fourmonth_agg:
            s_matrix = np.ones((4,),dtype=int)
            s_matrix = np.atleast_2d(s_matrix)
            s_matrix = np.concatenate((s_matrix,[[1,1,0,0]]))
            s_matrix = np.append(s_matrix, [[0,0,1,1]],axis = 0)
            s_matrix = np.concatenate((s_matrix,np.eye(4)))
        elif threemonth_agg:
            s_matrix = np.ones((3,),dtype=int)
            s_matrix = np.atleast_2d(s_matrix)
            s_matrix = np.concatenate((s_matrix,np.eye(3)))
        else:
            s_matrix = np.ones((2,),dtype=int)
            s_matrix = np.atleast_2d(s_matrix)
            s_matrix = np.concatenate((s_matrix,np.eye(2)))
        s_matrix = np.append(s_matrix,s_matrix,axis=0)
        s_matrix_low = s_matrix
        if semiannual_agg and not annual_agg:
            s_matrix = np.append(s_matrix,s_matrix,axis=0)
        elif not semiannual_agg and not annual_agg and fourmonth_agg:
            s_matrix = np.append(s_matrix,s_matrix,axis=0)
            s_matrix = np.append(s_matrix,s_matrix_low,axis=0)
        elif not semiannual_agg and not annual_agg and not fourmonth_agg and threemonth_agg:
            s_matrix = np.append(s_matrix,s_matrix,axis=0)
            s_matrix = np.append(s_matrix,s_matrix_low,axis=0)
            s_matrix = np.append(s_matrix,s_matrix_low,axis=0)
        elif not semiannual_agg and not annual_agg and not fourmonth_agg and not threemonth_agg:
            s_matrix = np.append(s_matrix,s_matrix,axis=0)
            s_matrix = np.append(s_matrix,s_matrix_low,axis=0)
            s_matrix = np.append(s_matrix,s_matrix,axis=0)
        return s_matrix

    def build_y_hat(self,predict_values,annual_agg,semiannual_agg,fourmonth_agg,threemonth_agg): 
        if annual_agg:
            forecast_number = 2
        elif semiannual_agg and not annual_agg:
            forecast_number = 4
        elif fourmonth_agg:
            forecast_number = 6
        elif threemonth_agg:
            forecast_number = 8
        else:
            forecast_number = 12
        for horizon in range(forecast_number):
            if not horizon:
                y_recon = predict_values[-1][horizon]
            else:
                y_recon = np.append(y_recon,predict_values[-1][horizon])
            for i in range(2,len(predict_values)+1):
                freq = int(len(predict_values[-i])/forecast_number)
                y_recon = np.append(y_recon,predict_values[-i][horizon*freq:(horizon+1)*freq])
        return y_recon
    
    def build_res(self,res_values,annual_agg,semiannual_agg,fourmonth_agg,threemonth_agg):
        res_length = len(res_values[-1])
        res_recon = []
        for year in range(res_length):
            res_recon_array = res_values[-1][year]
            for agg in range(2,len(res_values)+1):
                freq = int(len(res_values[-agg])/res_length)
                res_recon_array = np.append(res_recon_array,res_values[-agg][year*freq:(year+1)*freq])
            res_recon.append(res_recon_array)
        T = len(res_recon)
        for year in range(T):
            res_multi = np.dot(res_recon[year][None].T,res_recon[year][None])
            if not year:
                res_squared = np.asmatrix(res_multi)
            else:
                res_squared += np.asmatrix(res_multi)
        weight = 1/T * np.diag(res_squared)
        if annual_agg:
            agg_amount = 6
            agg_cutoff = [0,1,2,3,5,6,9,10,15,16,27]
        elif semiannual_agg:
            agg_amount = 4
            agg_cutoff = [0,1,2,3,5,6,11]
        elif fourmonth_agg:
            agg_amount = 3
            agg_cutoff = [0,1,2,3,6]
        elif threemonth_agg:
            agg_amount = 2
            agg_cutoff = [0,1,3]
        else:
            agg_amount = 2
            agg_cutoff = [0,1,2]
        for agg in range(agg_amount):
            if not agg:
                new_weight = weight[agg]
            else:
                avg_weight = np.ones(len(weight[agg_cutoff[(agg*2)-1]:agg_cutoff[agg*2]+1]))*np.mean(weight[agg_cutoff[(agg*2)-1]:agg_cutoff[agg*2]+1])
                new_weight = np.append(new_weight,avg_weight)
        weight = self.adjust_weight(weight,annual_agg,semiannual_agg,fourmonth_agg,threemonth_agg)
        weight = np.append(weight,weight)
        weight_low = weight
        if semiannual_agg and not annual_agg:
            weight = np.append(weight,weight)
        elif not semiannual_agg and not annual_agg and fourmonth_agg:
            weight = np.append(weight,weight)
            weight = np.append(weight,weight_low)
        elif not semiannual_agg and not annual_agg and not fourmonth_agg and threemonth_agg:
            weight = np.append(weight,weight)
            weight = np.append(weight,weight_low)
            weight = np.append(weight,weight_low)
        elif not semiannual_agg and not annual_agg and not fourmonth_agg and not threemonth_agg:
            weight = np.append(weight,weight)
            weight = np.append(weight,weight_low)
            weight = np.append(weight,weight)
        return res_recon,weight
        
    def adjust_weight(self,weight,annual_agg,semiannual_agg,fourmonth_agg,threemonth_agg):
        if annual_agg:
            agg_amount = 6
            agg_cutoff = [0,1,2,3,5,6,9,10,15,16,27]
        elif semiannual_agg:
            agg_amount = 4
            agg_cutoff = [0,1,2,3,5,6,11]
        elif fourmonth_agg:
            agg_amount = 3
            agg_cutoff = [0,1,2,3,6]
        elif threemonth_agg:
            agg_amount = 2
            agg_cutoff = [0,1,3]
        else:
            agg_amount = 2
            agg_cutoff = [0,1,2]
        for agg in range(agg_amount):
            if not agg:
                new_weight = weight[agg]
            else:
                avg_weight = np.ones(len(weight[agg_cutoff[(agg*2)-1]:agg_cutoff[agg*2]+1]))*np.mean(weight[agg_cutoff[(agg*2)-1]:agg_cutoff[agg*2]+1])
                new_weight = np.append(new_weight,avg_weight)
        return new_weight
        
    def grab_month(self,recon_p,annual_agg,semiannual_agg,fourmonth_agg,threemonth_agg):
        if annual_agg:
            frecon = recon_p[:int(len(recon_p)/2)]
            frecon = frecon[-12:]
            srecon = recon_p[int(len(recon_p)/2):]
            srecon = srecon[-12:]
            recon_fore = np.append(frecon,srecon) 
        elif semiannual_agg:
            fqrecon = recon_p[:int(len(recon_p)/4)]
            fqrecon = fqrecon[-6:]
            sqrecon = recon_p[:int(len(recon_p)/2)]
            sqrecon = sqrecon[-6:]
            tqrecon = recon_p[int(len(recon_p)/2):3*int(len(recon_p)/4)]
            tqrecon = tqrecon[-6:]
            lqrecon = recon_p[int(len(recon_p)/2):]
            lqrecon = lqrecon[-6:]
            recon_fore = np.append(fqrecon,sqrecon) 
            recon_fore = np.append(recon_fore,tqrecon)
            recon_fore = np.append(recon_fore,lqrecon)
        elif fourmonth_agg:
            trecon1 = recon_p[:int(len(recon_p)/6)]
            trecon1 = trecon1[-4:]
            trecon2 = recon_p[int(len(recon_p)/6):2*int(len(recon_p)/6)]
            trecon2 = trecon2[-4:]
            trecon3 = recon_p[2*int(len(recon_p)/6):3*int(len(recon_p)/6)]
            trecon3 = trecon3[-4:]
            trecon4 = recon_p[3*int(len(recon_p)/6):4*int(len(recon_p)/6)]
            trecon4 = trecon4[-4:]
            trecon5 = recon_p[4*int(len(recon_p)/6):5*int(len(recon_p)/6)]
            trecon5 = trecon5[-4:]
            trecon6 = recon_p[int(len(recon_p)/6):]
            trecon6 = trecon6[-4:]
            recon_fore = np.append(trecon1,trecon2) 
            recon_fore = np.append(recon_fore,trecon3)
            recon_fore = np.append(recon_fore,trecon4)
            recon_fore = np.append(recon_fore,trecon5)
            recon_fore = np.append(recon_fore,trecon6)
        elif threemonth_agg:
            quarcon1 = recon_p[:int(len(recon_p)/8)]
            quarcon1 = quarcon1[-3:]
            quarcon2 = recon_p[int(len(recon_p)/8):2*int(len(recon_p)/8)]
            quarcon2 = quarcon2[-3:]
            quarcon3 = recon_p[2*int(len(recon_p)/8):3*int(len(recon_p)/8)]
            quarcon3 = quarcon3[-3:]
            quarcon4 = recon_p[3*int(len(recon_p)/8):4*int(len(recon_p)/8)]
            quarcon4 = quarcon4[-3:]
            quarcon5 = recon_p[4*int(len(recon_p)/8):5*int(len(recon_p)/8)]
            quarcon5 = quarcon5[-3:]
            quarcon6 = recon_p[5*int(len(recon_p)/8):6*int(len(recon_p)/8)]
            quarcon6 = quarcon6[-3:]
            quarcon7 = recon_p[6*int(len(recon_p)/8):7*int(len(recon_p)/8)]
            quarcon7 = quarcon7[-3:]
            quarcon8 = recon_p[int(len(recon_p)/8):]
            quarcon8 = quarcon8[-3:]
            recon_fore = np.append(quarcon1,quarcon2) 
            recon_fore = np.append(recon_fore,quarcon3)
            recon_fore = np.append(recon_fore,quarcon4)
            recon_fore = np.append(recon_fore,quarcon5)
            recon_fore = np.append(recon_fore,quarcon6)
            recon_fore = np.append(recon_fore,quarcon7)
            recon_fore = np.append(recon_fore,quarcon8)
        else:
            bicon1 = recon_p[:int(len(recon_p)/12)]
            bicon1 = bicon1[-2:]
            bicon2 = recon_p[int(len(recon_p)/12):2*int(len(recon_p)/12)]
            bicon2 = bicon2[-2:]
            bicon3 = recon_p[2*int(len(recon_p)/12):3*int(len(recon_p)/12)]
            bicon3 = bicon3[-2:]
            bicon4 = recon_p[3*int(len(recon_p)/12):4*int(len(recon_p)/12)]
            bicon4 = bicon4[-2:]
            bicon5 = recon_p[4*int(len(recon_p)/12):5*int(len(recon_p)/12)]
            bicon5 = bicon5[-2:]
            bicon6 = recon_p[5*int(len(recon_p)/12):6*int(len(recon_p)/12)]
            bicon6 = bicon6[-2:]
            bicon7 = recon_p[6*int(len(recon_p)/12):7*int(len(recon_p)/12)]
            bicon7 = bicon7[-2:]
            bicon8 = recon_p[7*int(len(recon_p)/12):8*int(len(recon_p)/12)]
            bicon8 = bicon8[-2:]
            bicon9 = recon_p[8*int(len(recon_p)/12):9*int(len(recon_p)/12)]
            bicon9 = bicon9[-2:]
            bicon10 = recon_p[9*int(len(recon_p)/12):10*int(len(recon_p)/12)]
            bicon10 = bicon10[-2:]
            bicon11 = recon_p[10*int(len(recon_p)/12):11*int(len(recon_p)/12)]
            bicon11 = bicon11[-2:]
            bicon12 = recon_p[int(len(recon_p)/12):]
            bicon12 = bicon12[-2:]
            recon_fore = np.append(bicon1,bicon2) 
            recon_fore = np.append(recon_fore,bicon3)
            recon_fore = np.append(recon_fore,bicon4)
            recon_fore = np.append(recon_fore,bicon5)
            recon_fore = np.append(recon_fore,bicon6)
            recon_fore = np.append(recon_fore,bicon7)
            recon_fore = np.append(recon_fore,bicon8)
            recon_fore = np.append(recon_fore,bicon9)
            recon_fore = np.append(recon_fore,bicon10)
            recon_fore = np.append(recon_fore,bicon11)
            recon_fore = np.append(recon_fore,bicon12)
        recon_fore[recon_fore<0] = 0
        return recon_fore
    