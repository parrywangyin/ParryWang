from xml.dom import minidom
content = ''' <?xml version="1.0" encoding="UTF-8"?>
  <ShowInventory xmlns="ODM://built-in//show_inventory">
    <SpecVersion>built-in</SpecVersion>
    <InventoryEntry>
      <ChassisName>&quot;c38xx Stack&quot;</ChassisName>
      <Description>&quot;c38xx Stack&quot;</Description>
      <PID>WS-C3850-48F-S</PID>
      <VID>V07</VID>
      <SN>FOC2124L4SQ</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;Switch 1&quot;</ChassisName>
      <Description>&quot;WS-C3850-48F-S&quot;</Description>
      <PID>WS-C3850-48F-S</PID>
      <VID>V07</VID>
      <SN>FOC2124L4SQ</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;StackPort1/1&quot;</ChassisName>
      <Description>&quot;StackPort1/1&quot;</Description>
      <PID>STACK-T1-50CM</PID>
      <VID>V01</VID>
      <SN>MOC2126A1CM</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;StackPort1/2&quot;</ChassisName>
      <Description>&quot;StackPort1/2&quot;</Description>
      <PID>STACK-T1-50CM</PID>
      <VID>V01</VID>
      <SN>MOC2122A4L6</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;Switch 1 - Power Supply A&quot;</ChassisName>
      <Description>&quot;Switch 1 - Power Supply A&quot;</Description>
      <PID>PWR-C1-1100WAC</PID>
      <VID>V02</VID>
      <SN>LIT21224HGX</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;Switch 1 - Power Supply B&quot;</ChassisName>
      <Description>&quot;Switch 1 - Power Supply B&quot;</Description>
      <PID>PWR-C1-1100WAC</PID>
      <VID>V02</VID>
      <SN>LIT21212QKT</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;Switch 1 FRU Uplink Module 1&quot;</ChassisName>
      <Description>&quot;2x1G 2x10G Uplink Module&quot;</Description>
      <PID>C3850-NM-2-10G</PID>
      <VID>V01</VID>
      <SN>FOC212498XR</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;Te1/1/4&quot;</ChassisName>
      <Description>&quot;SFP-10GBase-SR&quot;</Description>
      <PID>SFP-10G-SR</PID>
      <VID>V03</VID>
      <SN>AVD1849ALDU     </SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;Switch 2&quot;</ChassisName>
      <Description>&quot;WS-C3850-48F-S&quot;</Description>
      <PID>WS-C3850-48F-S</PID>
      <VID>V07</VID>
      <SN>FOC2128L412</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;StackPort2/1&quot;</ChassisName>
      <Description>&quot;StackPort2/1&quot;</Description>
      <PID>STACK-T1-50CM</PID>
      <VID>V01</VID>
      <SN>MOC2122A4L6</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;StackPort2/2&quot;</ChassisName>
      <Description>&quot;StackPort2/2&quot;</Description>
      <PID>STACK-T1-50CM</PID>
      <VID>V01</VID>
      <SN>MOC2126A1CM</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;Switch 2 - Power Supply A&quot;</ChassisName>
      <Description>&quot;Switch 2 - Power Supply A&quot;</Description>
      <PID>PWR-C1-1100WAC</PID>
      <VID>V02</VID>
      <SN>DTN2122V3DE</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;Switch 2 - Power Supply B&quot;</ChassisName>
      <Description>&quot;Switch 2 - Power Supply B&quot;</Description>
      <PID>PWR-C1-1100WAC</PID>
      <VID>V02</VID>
      <SN>DTN2122V3DB</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;Switch 2 FRU Uplink Module 1&quot;</ChassisName>
      <Description>&quot;2x1G 2x10G Uplink Module&quot;</Description>
      <PID>C3850-NM-2-10G</PID>
      <VID>V01</VID>
      <SN>FOC21273BR4</SN>
    </InventoryEntry>
    <InventoryEntry>
      <ChassisName>&quot;Te2/1/4&quot;</ChassisName>
      <Description>&quot;SFP-10GBase-SR&quot;</Description>
      <PID>SFP-10G-SR</PID>
      <VID>V03</VID>
      <SN>AVD1849AACX</SN>
    </InventoryEntry>
  </ShowInventory>
'''
doc = minidom.parseString(content).getElementsByTagName('InventoryEntry')
print (doc)
