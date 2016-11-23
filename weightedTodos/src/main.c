/*
 * MAIN FILE
 *
 * blah blah blah 
 *
 */

#define YEAR(a)  ((a>>9) & (0x008FFFFF))
#define MONTH(a) ((a>>5) & (0x0000000F))
#define DAY(a)   (a & (0x0000001F))

#define SETDATE(y, m, d) (((y & 0x008FFFFF) << 9) | ((m & 0x0000000F) << 5) | (d & 0x0000001F))

typedef struct todoitem {
  char finished;
  char name[60];
  int startdate;  //
  int duedate;    //0b<year 23bits><month 4bits><day 5bits> 
  int assignDate;
} t_todo;

typedef struct day{
  int day;
  char minutes[1440];
}t_day;

typedef struct week{
  int weekdate;//Sunday of the week
  t_day days[7]; //[sunday, monday,...,saturday]
}t_week;

int openSch(){
  
}

int saveSch(){

}


int main(void){


}
