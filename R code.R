data=read.csv(choose.files(),header = TRUE)
# Load required library
library(ggplot2)
df=data
# Assuming your data is stored in a data frame named df
# If 'Proportion_by_party' is not numeric, convert it to numeric
df$Proportion_by_party <- as.numeric(df$Proportion_by_party)
# Create boxplot
ggplot(df, aes(x = Party, y = Proportion_by_party)) +
  geom_boxplot() +
  labs(title = "Proportions by Party",
       x = "Party",
       y = "Proportion by Party") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))  # Rotate x-axis labels for better readability
# Load required library
library(ggplot2)
# Create boxplot with customized colors
ggplot(df, aes(x = Party, y = Proportion_by_party, fill = Party)) +
  geom_boxplot() +
  labs(title = "Proportions by Party",
       x = "Party",
       y = "Proportion by Party") +
  scale_fill_manual(values = c("red", "blue", "green")) +  # Set custom colors
  theme(axis.text.x = element_text(angle = 45, hjust = 1))  # Rotate x-axis labels for better readability
# Create boxplot with customized colors
ggplot(df, aes(x = Party, y = Proportion_by_party, fill = Party)) +
  geom_boxplot() +
  labs(title = "Proportions by Party All Elections",
       x = "Party",
       y = "Proportion by Party") +
  scale_fill_manual(values = c("red", "blue", "green")) +  # Set custom colors
  theme(axis.text.x = element_text(angle = 45, hjust = 1))  # Rotate x-axis labels for better readability
df=read.csv(choose.files(),header = TRUE)
# Create boxplot with customized colors
ggplot(df, aes(x = Party, y = Proportion_by_party, fill = Party)) +
  geom_boxplot() +
  labs(title = "Proportions by Party",
       x = "Party",
       y = "Proportion by Party") +
  scale_fill_manual(values = c("red", "blue", "green")) +  # Set custom colors
  theme(axis.text.x = element_text(angle = 45, hjust = 1))  # Rotate x-axis labels for better readability
