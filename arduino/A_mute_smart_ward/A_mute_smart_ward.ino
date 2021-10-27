const int led = 11;
const int led1 = 12;
const int led2 = 13;

int receivedData = 0;

void setup()
{
  pinMode(led, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  digitalWrite (led, LOW);
  digitalWrite (led1, LOW);
  digitalWrite (led2, LOW);
  Serial.begin(9600);
  Serial.println("Connected Successfully");
}

void loop(){
  
  while(Serial.available())
  {
    receivedData = Serial.read();
  }
  
  if (receivedData == 'd')
  {
    digitalWrite (led, HIGH);
    digitalWrite (led1, LOW);
    digitalWrite (led2, LOW);
  }
  else if (receivedData == 'c')
  {
    digitalWrite (led, LOW);
    digitalWrite (led1, HIGH);
    digitalWrite (led2, LOW);
  }
  else if (receivedData == 'r')
  {
    digitalWrite (led, LOW);
    digitalWrite (led1, LOW);
    digitalWrite (led2, HIGH);
  }
}
