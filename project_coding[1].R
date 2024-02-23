
data=read.csv("C:\\Users\\aksha\\Documents\\Temporary work\\coding data\\coding file all seats by proportion(BJP&INC&Other).csv",header = T)
df <- data
str(df)
colnames(df)[7] <- "Party"
df$State_Name <- as.factor(df$State_Name)
df$Party <- as.factor(df$Party)
df$Constituency_Name <- as.factor(df$Constituency_Name)
df$Proportion_by_party <- df$Votes/df$Valid_Votes

df_bjp <- df[df$Party == "BJP",]
df_inc <- df[df$Party == "INC",]
df_oth <- df[df$Party == "Other",]

# BJP
df_bjp_up <- df_bjp[df_bjp$State_Name == "Uttar_Pradesh",]
df_bjp_agra <- df_bjp[df_bjp$Constituency_Name == "AGRA",]

plot(df_bjp_agra$Year ~ df_bjp_agra$Proportion_by_party, type = "l", lwd = 2) 
lines()

# INC
df_INC_maharashtra <- df_inc[df_inc$State_Name == "Maharashtra",]
df_INC_nagpur <- df_inc[df_inc$Constituency_Name == "NAGPUR",]

plot(df_INC_nagpur$Year ~ df_INC_nagpur$Proportion_by_party, type = "l", lwd = 2) 

# Other

df_other_Andaman <- df_oth[df_oth$State_Name == "Andaman_&_Nicobar_Islands",]
df_other_andaman <- df_oth[df_oth$Constituency_Name == "ANDAMAN & NICOBAR ISLANDS",]

plot(df_other_andaman$Year ~ df_other_andaman$Proportion_by_party, type = "l", lwd = 2) 


# INC
df_INC_maharashtra <-df_bjp[df_bjp$State_Name == "Maharashtra",]
df_INC_satara <- df_bjp[df_bjp$Constituency_Name == "SATARA",]
plot(df_INC_satara$Year ~ df_INC_satara$Proportion_by_party, type = "l", lwd = 2) 

  
generate_plot <- function(Constituency_Name, df) 
  {
  df_bjp <- df[df$Party == "BJP", ]
  df_inc <- df[df$Party == "INC", ]
  df_oth <- df[df$Party == "Other", ]
  
  df_con_bjp <- df_bjp[df_bjp$Constituency_Name == Constituency_Name, ]
  df_con_inc <- df_inc[df_inc$Constituency_Name == Constituency_Name, ]
  df_con_oth <- df_oth[df_oth$Constituency_Name == Constituency_Name, ]
  
  plot(df_con_bjp$Year, df_con_bjp$Proportion_by_party, type = "l", lwd = 2, col = "darkred",
       main = paste("Proportion by party in", Constituency_Name),
       xlab = "Year", ylab = "Proportion by party", xlim = c(1962, 2019),ylim=c(0,1))
  
  lines(df_con_inc$Year, df_con_inc$Proportion_by_party, type = "l", lwd = 2, col = "black")
  
  lines(df_con_oth$Year, df_con_oth$Proportion_by_party, type = "l", lwd = 2, col = "darkblue")
  
  legend("topright", legend = c("BJP", "INC", "Other"), col = c("darkred", "black", "darkblue"), lty = 1, cex = 0.6)
}

generate_plot("ANAND", df)
  



















