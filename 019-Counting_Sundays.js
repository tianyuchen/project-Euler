// You are given the following information, but you may prefer to do some
// research for yourself.
//
// 1 Jan 1900 was a Monday.
// Thirty days has September,
// April, June and November.
// All the rest have thirty-one,
// Saving February alone,
// Which has twenty-eight, rain or shine.
// And on leap years, twenty-nine.
// A leap year occurs on any year evenly divisible by 4, but not on a century
// unless it is divisible by 400.
// How many Sundays fell on the first of the month during the twentieth century
// (1 Jan 1901 to 31 Dec 2000)?

/**
 * Count number of Sundays fell on 1st of months between years
 * @param {number} start year
 * @param {number} end year
 * @return {number} number of sundays
 */
function countSundays(start, end) {
  let sundays = 0;
  for (let year = start; year <= end; ++year) {
    for (let month = 0; month < 12; ++month) {
      // getDay() returns between 0 and 6 (0 being Sunday, 6 being Saturday)
      if (new Date(year, month, 1).getDay() == 0) {
        sundays++;
      }
    }
  }
  return sundays;
}

console.log(countSundays(1901, 2000));
