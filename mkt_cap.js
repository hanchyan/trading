// this is really an Apps Script (.gs) not a .js. This script is for recording the daily market cap
// of all the stocks in the S and P 500 for index price analysis purposes 

function recordMarketCapForTickers() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var tickers = sheet.getRange("A2:A").getValues().filter(String); // Get all tickers from column A
  var today = new Date();
  
  // Find the next blank column by checking row 1 (headers) for the first empty cell
  var lastColumn = sheet.getLastColumn();
  var nextColumn = lastColumn + 1;
  
  // Ensure that the next available column is really blank
  while (sheet.getRange(1, nextColumn).getValue() !== '') {
    nextColumn++;
  }
  
  Logger.log('Next column: ' + nextColumn); // Log the next column number

  // Set today's date in the new column (row 1)
  sheet.getRange(1, nextColumn).setValue(today).setNumberFormat("yyyy-mm-dd");
  
  // Loop through each ticker and get its market cap
  for (var i = 0; i < tickers.length; i++) {
    var ticker = tickers[i][0]; // Get the ticker symbol
    if (ticker) {
      Logger.log('Processing ticker: ' + ticker); // Log each ticker
      var marketCapFormula = '=GOOGLEFINANCE("' + ticker + '", "marketcap")';
      var row = i + 2; // Start writing market caps from row 2
      
      // Set the formula to retrieve market cap
      sheet.getRange(row, nextColumn).setFormula(marketCapFormula);
      
      // Delay to allow the formula to update and fetch the value
      Utilities.sleep(3000);
      
      // Replace the formula with the actual market cap value (static)
      var marketCapValue = sheet.getRange(row, nextColumn).getValue();
      Logger.log('Market Cap for ' + ticker + ': ' + marketCapValue); // Log the market cap value
      sheet.getRange(row, nextColumn).setValue(marketCapValue); // Set the static value
    }
  }
}
// Test 

