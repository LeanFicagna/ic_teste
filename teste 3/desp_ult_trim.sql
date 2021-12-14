USE banco_ans;

select REG_ANS, DESCRICAO, truncate((sum(cast(REPLACE(VL_SALDO_FINAL,',','.') as float))), 2)  
				'despesas com EVENTOS/ SINISTROS CON...MEDICO HOSPITALAR' from t_dados
where DESCRICAO like 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ' and
STR_TO_DATE(D_DATA, '%e/%c/%Y') between '2021-06-01' and '2021-09-01'
group by REG_ANS
order by sum(cast(REPLACE(VL_SALDO_FINAL,',','.') as float)) desc
limit 10;