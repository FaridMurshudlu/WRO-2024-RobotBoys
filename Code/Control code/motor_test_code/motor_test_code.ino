// Define the motor control pins
#define IN1 8  // Motor direction pin 1
#define IN2 9  // Motor direction pin 2
#define ENA 10 // Motor speed pin (PWM)

// Define the motor speed (0-255)
int motorSpeed = 150;

void setup() {
  // Set motor control pins as output
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);
  
  // Initialize serial communication for debugging
  Serial.begin(9600);
}

void loop() {
  // Forward direction
  Serial.println("Motor moving forward");
  digitalWrite(IN1, HIGH); // Set IN1 HIGH
  digitalWrite(IN2, LOW);  // Set IN2 LOW
  analogWrite(ENA, motorSpeed); // Set motor speed
  delay(2000); // Run for 2 seconds

  // Stop the motor
  Serial.println("Motor stopped");
  analogWrite(ENA, 0); // Set speed to 0
  delay(1000); // Wait for 1 second

  // Reverse direction
  Serial.println("Motor moving backward");
  digitalWrite(IN1, LOW);  // Set IN1 LOW
  digitalWrite(IN2, HIGH); // Set IN2 HIGH
  analogWrite(ENA, motorSpeed); // Set motor speed
  delay(2000); // Run for 2 seconds

  // Stop the motor again
  Serial.println("Motor stopped");
  analogWrite(ENA, 0); // Set speed to 0
  delay(1000); // Wait for 1 second
}
