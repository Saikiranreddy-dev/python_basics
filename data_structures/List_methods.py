# strings immuatbele
name="sai"
student=name
name="kiran"
# now name is change the string points to different now
#but the student is points to name before changed only

scores=['b','c','a','d','b','a']
grades=scores
# list are mutable so if i change the scores grades will also
# changes since both points scores and grades same addess
scores[2]='b'
print("scores:"+str(scores))
print("grades"+str(grades))
print(max(scores))
print(min(scores))
print(len(scores))
# sorted creates another list but not change the original list
#scores=sorted(scores,reverse=True) permanently points to scores with this list
print(sorted(scores,reverse=True))

#join method
string="\n".join(scores)
st="-".join(["garcia","O'kelly"])


print(string+"\n"+st)
# append method
scores.append(9)
print(scores)