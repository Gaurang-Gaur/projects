# wap to find double space in program.
str="It contain double space  in str."
ds=str.find("  ")# while using any function in string in python i have to save the change
# in new variable show it can show amendment in new variable after using function.
str=str.replace("  "," ")
print(ds)
print(str)