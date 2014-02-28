bag = Hash.new(0)
$stdin.each do |line|
	line.chomp!
	line.downcase!
	line.gsub!(/[^a-zA-Z\s]/,"")
	line.sub!(/^[\s]+/, "")
	line.squeeze!(" ")
	words = line.split(/ +/)
	words.each do |word|
		bag[word] += 1
	end
end

bag.select!{|key, value| value >= 2}

pairs = bag.sort do |pair1, pair2|
	if pair1[1] == pair2[1]
		pair1[0] <=> pair2[0]
	else
		pair2[1] <=> pair1[1]
	end
end

longest = pairs.inject(0) do |l, v|
    v[0].length > l ? v[0].length : l
end

pairs.each do |pair|
	printf "%-*.*s ", longest, longest, pair[0]
    #puts "word \'#{pair[0]}\' occurs #{pair[1]} times"
    puts "*" * pair[1]
end
