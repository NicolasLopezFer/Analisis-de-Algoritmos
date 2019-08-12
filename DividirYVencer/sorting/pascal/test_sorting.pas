program Hello;

uses sysutils, DateUtils, UBubbleSort;

var
   a              : array of integer; (* a 2 dimensional array *)
   i, n           : integer;
   s_time, e_time : TDateTime;
              
begin
   Randomize;
   n := 1000000;
   setlength( a, n );
   for i := 0 to n - 1 do
   begin
      a[ i ] := Random( 2 * n );
   end;

   s_time := Now;
   BubbleSort( a );
   e_time := Now;
   writeln( MilliSecondsBetween( s_time, e_time ) );
end.

(* eof - test_sorting.pas *)
