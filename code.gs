
function onEdit(e) {
    
    var value = e.value;

    var payload = {
      range: range.getA1Notation(),
      value: value,
      sheetName: sheet.getName(),
      row: row,
      productID: productID  
    };

    var options = {
      'method': 'post',
      'contentType': 'application/json',
      'payload': JSON.stringify(payload)
    };

   
    var url = 'https://1d0b-2406-7400-113-aac5-f01a-2e21-fd96-28f1.ngrok-free.app/sync'; 

    UrlFetchApp.fetch(url, options);
  
}

// Function to handle structural changes in the sheet
function onChange(e) {
  console.log(e.changeType);
  if (e.changeType == 'REMOVE_ROW') {
    var sheet = e.source.getActiveSheet();
    var productIDs = sheet.getRange("A2:A").getValues().flat();
    console.log(productIDs);
    // Compare current product IDs with a stored list (requires maintaining a state)
    var previousProductIDs = getPreviousProductIDs();
    var deletedIDs = previousProductIDs.filter(id => !productIDs.includes(id));
    
    deletedIDs.forEach(function(productID) {
      var deletePayload = {
        productID: productID
      };
      
      var deleteOptions = {
        'method': 'post',
        'contentType': 'application/json',
        'payload': JSON.stringify(deletePayload)
      };

      var deleteUrl = 'https://1d0b-2406-7400-113-aac5-f01a-2e21-fd96-28f1.ngrok-free.app/delete_row';
      console.log(deleteOptions);
      UrlFetchApp.fetch(deleteUrl, deleteOptions);
    });

    // Update the stored product IDs
    setPreviousProductIDs(productIDs);
  }
}

// Helper functions to store and retrieve Product IDs
function getPreviousProductIDs() {
  var scriptProperties = PropertiesService.getScriptProperties();
  var productIDs = scriptProperties.getProperty('previousProductIDs');
  return productIDs ? JSON.parse(productIDs) : [];
}

function setPreviousProductIDs(productIDs) {
  var scriptProperties = PropertiesService.getScriptProperties();
  scriptProperties.setProperty('previousProductIDs', JSON.stringify(productIDs));
}
