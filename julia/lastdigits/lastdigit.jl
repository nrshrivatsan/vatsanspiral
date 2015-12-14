a = Int64[]
freq = Dict()
p = primes(900012)
for n in p[5:]
  push!(a,n%10)
  #print(n%10)
end

c = 0
for i in a
  c+=1
  print(i)
  if c == 4
    c=0
    print(',')
  end
end
println()
