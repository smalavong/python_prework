my_dict = {
    "name":"Troy Aikman",
    "position":"QB",
    "team":"Dallas Cowboys",
    "age": 54,
    "weight": 220.,
    "superbowls":["XXVII","XXVIII","XXX"],
    "awards":{
        "super_bowl_mvp":"XXVII",
        "probowl":[1991, 1992, 1993, 1994, 1995, 1996],
        "man_of_the_year":1997
        }
}
     
a_list=[]
for k, v in my_dict["awards"].items():
    if k =="super_bowl_mvp" or k == "man_or_the_year":
        a_list.append(v)
print(a_list) 