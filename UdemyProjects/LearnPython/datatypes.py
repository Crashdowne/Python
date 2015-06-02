a = 50
print(type(a),a);

b = 90.2;
print(type(b),b);

c = int(90.4);
print(type(c),c);

d = "This is a string \nConvert to a raw string \\n";
print(type(d),d);

#! \n is an escape character -> new line
#! \\n -> converts an escape character to a raw string
#! {} is used to insert data into a string (used in conjunction with .format()

e = "*Inserted text*";
f = "This is a {} string".format(e);
print(f);

#! lists = Array -> nrml array
#! tuple = Array -> cannot be modified after created

g = (1,2,3,4,5);
print(type(g),g);

h = [1,2,3,4,5];
h.append(6);
print(type(h),h)
print("Value at location 2 is:",h[2]);
print("Values at locations 1 - 4 are:",h[1:4]);

#! Dictionary -> Key and value (hashed list)

i = {"one":1,"two":2}
print(type(i),i)

dictionary = dict(
                  one = 1, 
                  two = 2)
print(dictionary)

boolean = False
print(boolean)

j = 0
k = 1

if j==k: 
    print(True)
else:
    print(False)
    













