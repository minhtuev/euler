con = 10000000000
add a b = rem (a + b) con
mul a b = rem (a * b) con
pow a 1 = mul a 1
pow a n = mul a (pow a (n - 1))
cal = sum . map (\x -> (pow x x))
main = print(rem (cal [1..1000]) con)