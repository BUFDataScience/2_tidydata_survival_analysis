NAME: 
Worcester Heart Attack Study WHAS500 Data (whas500.dat)

SIZE: 
500 Observations, 22 variables

SOURCE: 
Worcester Heart Attack Study data from Dr. Robert J. Goldberg of 
the Department of Cardiology at the University of Massachusetts Medical 
School. 

REFERENCE:
Hosmer, D.W. and Lemeshow, S. and May, S. (2008) 
Applied Survival Analysis: Regression Modeling of Time to Event Data:
Second Edition, John Wiley and Sons Inc., New York, NY

DESCRIPTIVE ABSTRACT:
The main goal of this study is to describe factors associated 
with trends over time in the incidence and survival rates following 
hospital admission for acute myocardial infarction (MI).  Data have been 
collected during thirteen 1-year periods beginning in 1975 and extending 
through 2001 on all MI patients admitted to hospitals in the Worcester, 
Massachusetts Standard Metropolitan Statistical Area.

DISCLAIMER:  
This data is also available at the following Wiley's FTP site: 
ftp//ftp.wiley.com/public/sci_tech_med/survival

LIST OF VARIABLES:

Variable 	Name		Description			        Codes / Values
*******************************************************************************************************
1		id		Identification Number			1 - 500
2		age		Age at Hospital Admission		Years
3 		gender		Gender 					0 = Male, 1 = Female
4 		hr		Initial Heart Rate			Beats per minute
5		sysbp		Initial Systolic Blood Pressure 	mmHg
6		diasbp		Initial Diastolic Blood Pressure	mmHg
7 		bmi		Body Mass Index			 	kg/m^2
8		cvd		History of Cardiovascular Disease	0 = No, 1 = Yes						
9		afb		Atrial Fibrillation			0 = No, 1 = Yes						
10		sho		Cardiogenic Shock			0 = No, 1 = Yes						
11		chf		Congestive Heart Complications		0 = No, 1 = Yes						
12		av3		Complete Heart Block			0 = No, 1 = Yes				
13		miord		MI Order 				0 = First, 1 = Recurrent
14		mitype		MI Type 				0 = non Q-wave, 1 = Q-wave
15		year		Cohort Year				1 = 1997, 2 = 1999, 3 = 2001				
16		admitdate	Hospital Admission Date 		mm/dd/yyyy
17		disdate		Hospital Discharge Date 		mm/dd/yyyy
18		fdate		Date of last Follow Up 			mm/dd/yyyy
19		los		Length of Hospital Stay			Days from Hospital Admission
								 	  to Hospital Discharge
20 		dstat		Discharge Status from Hospital		0 = Alive, 1 = Dead
21		lenfol		Total Length of Follow-up		Days from Hospital Admission Date
									  to Date of Last Follow-up 
22		fstat		Vital Status at Last Follow-up		0 = Alive 1 = Dead
