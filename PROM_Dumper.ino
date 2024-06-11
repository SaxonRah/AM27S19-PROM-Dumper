// Define address and data pins
const int addressPins[] = {2, 3, 4, 5, 6}; // A0 to A4
const int dataPins[] = {8, 9, 10, 11, 12, 13, A0, A1}; // Q0 to Q7
const int oePin = 7; // Output Enable

void setup() {
  // Initialize address pins as outputs
  for (int i = 0; i < 5; i++) {
    pinMode(addressPins[i], OUTPUT);
  }

  // Initialize data pins as inputs
  for (int i = 0; i < 8; i++) {
    pinMode(dataPins[i], INPUT);
  }

  // Initialize control pin
  pinMode(oePin, OUTPUT);

  // Set control pin to default state
  digitalWrite(oePin, HIGH); // Disable output

  Serial.begin(9600); // Start serial communication
}

void loop() {
  // Enable output
  digitalWrite(oePin, LOW);

  // Loop through all addresses (32 addresses for 32x8 ROM)
  for (unsigned int address = 0; address < 32; address++) {
    // Set address pins
    for (int i = 0; i < 5; i++) {
      digitalWrite(addressPins[i], (address >> i) & 1);
    }

    delayMicroseconds(1); // Small delay for address to settle

    // Read data pins
    byte data = 0;
    for (int i = 0; i < 8; i++) {
      data |= digitalRead(dataPins[i]) << i;
    }

    // Create Intel HEX record
    byte recordLength = 1; // 1 byte of data
    byte recordType = 0; // Data record
    byte checksum = recordLength + (address >> 8) + (address & 0xFF) + recordType + data;
    checksum = ~checksum + 1;

    // Output Intel HEX formatted string
    Serial.print(":");
    printHex(recordLength);
    printHex((address >> 8) & 0xFF);
    printHex(address & 0xFF);
    printHex(recordType);
    printHex(data);
    printHex(checksum);
    Serial.println();
  }

  // Disable output
  digitalWrite(oePin, HIGH);

  while (true); // Stop after one pass
}

void printHex(byte value) {
  if (value < 16) {
    Serial.print('0');
  }
  Serial.print(value, HEX);
}
