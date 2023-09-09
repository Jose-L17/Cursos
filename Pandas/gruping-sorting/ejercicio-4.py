sorted_varieties = reviews.groupby('variety').price.agg([min,max]).sort_values(by=['min', 'max'], ascending=False)

# Check your answer
print(sorted_varieties)
