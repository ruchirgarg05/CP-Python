# Initialize 2d array
arr = Array.new(2) {Array.new(2,5)} #=> [[5,5],[5,5]]

# if else 
if cond
  # do something
  pass
elsif
  # do something else
end  

# for loop

arr = [1,2,3]
for num in arr
  puts num # 1, 2, 3
end  

for i in 1..arr.length()-1
  puts arr[i]
end

# Accessing a 2d 3x3 grid from a 9x9 board
grid = board[i..i+2].map { |row| row[j..j+2] }

# to flatten
row = grid.flatten

