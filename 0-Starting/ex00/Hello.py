ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "UAE!")
ft_set = (ft_set - {"tutu!"}) | {"Abu Dhabi!"}
ft_dict["Hello"] = "42 Abu Dhabi!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# ft_tuple = tuple(list(ft_tuple)[:1] + ["UAE!"])

# ft_set.remove("tutu!")
# ft_set.add("Abu Dhabi!")
