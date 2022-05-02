#include <Servo.h>
#define n 5
#define digits 1
Servo h1;
Servo h2;
Servo h3;
Servo h4;
Servo h5;
int valrec[n];
int slen=n*digits+1;
int count=0;
bool c=false;
String rec;
void rd(){
while(Serial.available()){
char c=Serial.read();
if(c=='$'){
c=true;
}
11
if(c){
if(count<slen){
rec = String(rec+c);
count++;
}
if(count>=slen){
for(int i=0;i<n;i++){
int num=(i*digits)+1;
valrec[i]=rec.substring(num,num+digits).toInt();
}
rec="";
count=0;
c=false;
}
}
}
}
void setup() {
// put your setup code here, to run once:
Serial.begin(9600);
h1.attach(10);
 h2.attach(9);
 h3.attach(8);
 h4.attach(7);
 h5.attach(6);
}
void loop() {
// put your main code here, to run repeatedly:
rd();
if(valrec[0]==1){h1.write(180);}else{h1.write(0);}
if(valrec[1]==1){h2.write(180);}else{h2.write(0);}
if(valrec[2]==1){h3.write(180);}else{h3.write(0);}
if(valrec[3]==1){h4.write(180);}else{h4.write(0);}
if(valrec[4]==1){h5.write(180);}else{h5.write(0);}
}
