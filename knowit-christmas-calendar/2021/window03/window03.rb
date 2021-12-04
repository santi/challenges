data = File.read("input.txt").strip()

lookup = {
    0 => 0
}
running_sum = 0
max = 0
maxIndex = -1
data.split("").each_with_index { |val, index| 
    if val == 'J'
        running_sum += 1
    else
        running_sum -= 1
    end

    if lookup.key?(running_sum) && index - lookup[running_sum] > max
        max = index - lookup[running_sum]
        maxIndex = lookup[running_sum] + 1
    end

    if !lookup.key?(running_sum)
        lookup[running_sum] = index
    end
}

puts "#{max}, #{maxIndex}"

