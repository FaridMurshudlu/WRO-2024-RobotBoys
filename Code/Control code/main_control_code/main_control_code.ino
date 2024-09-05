// Define pin connections for 3 ultrasonic sensors
#define TRIG_PIN1 9  // Trigger pin for Sensor 1
#define ECHO_PIN1 10 // Echo pin for Sensor 1
#define TRIG_PIN2 11 // Trigger pin for Sensor 2
#define ECHO_PIN2 12 // Echo pin for Sensor 2
#define TRIG_PIN3 13 // Trigger pin for Sensor 3
#define ECHO_PIN3 A0 // Echo pin for Sensor 3

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set the trigger pins as OUTPUT and the echo pins as INPUT
  pinMode(TRIG_PIN1, OUTPUT);
  pinMode(ECHO_PIN1, INPUT);
  pinMode(TRIG_PIN2, OUTPUT);
  pinMode(ECHO_PIN2, INPUT);
  pinMode(TRIG_PIN3, OUTPUT);
  pinMode(ECHO_PIN3, INPUT);

  // Ensure the trigger pins are initially LOW
  digitalWrite(TRIG_PIN1, LOW);
  digitalWrite(TRIG_PIN2, LOW);
  digitalWrite(TRIG_PIN3, LOW);
  delay(1000); // Wait for sensors to stabilize
}

void loop() {
  // Read distances from all 3 sensors
  long distance1 = getDistance(TRIG_PIN1, ECHO_PIN1);
  long distance2 = getDistance(TRIG_PIN2, ECHO_PIN2);
  long distance3 = getDistance(TRIG_PIN3, ECHO_PIN3);

  // Print the distances to the Serial Monitor
  Serial.print("Sensor 1 Distance: ");
  Serial.print(distance1);
  Serial.println(" cm");

  Serial.print("Sensor 2 Distance: ");
  Serial.print(distance2);
  Serial.println(" cm");

  Serial.print("Sensor 3 Distance: ");
  Serial.print(distance3);
  Serial.println(" cm");

  // Wait for a short time before repeating
  delay(500);
}

// Function to measure distance for a given sensor
long getDistance(int trigPin, int echoPin) {
  // Send a 10 microsecond pulse to the trigger pin
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure the time it takes for the echo to return
  long duration = pulseIn(echoPin, HIGH);

  // Calculate the distance in centimeters
  long distance = duration * 0.034 / 2;

  return distance;
}
