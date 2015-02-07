#!/usr/bin/perl
for $i (1, 2, 3, 4, 5) {
	print "$i\n";
}

for $k ("lokesh", "aarav", "swati") {
	print "$k\n";
}
@one_to_ten = (1 .. 10);
    $top_limit = 25;
    for $i (@one_to_ten, 15, 20 .. $top_limit) {
        print "$i\n";
    }
%days_in_summer = ( "July" => 31, "August" => 31, "September" => 30 );
