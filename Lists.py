IEEE_Society = ["CS", "WIE", "RAS", "AESS", "CIS"]
MemberOfSociety = [100, 45, 20, 30, 25]
for i in range(0, len(IEEE_Society)):
    print(MemberOfSociety[i], "members are part of the ", IEEE_Society[i])

# 3rd step is "list" (array)
ieee_List = ["aess", "cis", "cs", "ras", "wie"]
print(ieee_List)
print(ieee_List[0], " ", ieee_List[:3], " ", ieee_List[2:], " ", ieee_List[1:3])
print(len(ieee_List))
#len() = length

ieee_List.append("ias")
print(ieee_List)
ieee_List.pop()
print(ieee_List)
ieee_List.insert(1, "ias")
print(ieee_List)
ieee_List.remove("aess")
print(ieee_List)
print(type(ieee_List))


del ieee_List[2:4]
print(ieee_List)
ieee_List.clear()
print(ieee_List)
ieee_List = list(("aess", "cis", "cs", "ras", "wie"))
print(ieee_List)