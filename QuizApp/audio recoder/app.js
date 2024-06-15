const display = document.querySelector('.display')
const controllerWrapper = document.querySelector('.controllers'),

const State = ['Initial', 'Record', 'Download']
let stateIndex = 0
let mediaRecorder, chunks = [], audioURL = '',

const application = (index) => {
  switch (State[index]){
    case 'Initial':
     clearDisplay() 
     clearControls()
     addMessage( 'Press the start button to start recording') 
     addButton('record', 'record(', 'Start Recording')
      break;
   case 'Record':
     clearDisplay() 
     clearControls() 
     addMessage( 'Recording...') 
     addButton('stop', 'stopRecording()', 'Stop Recording')
     break
   case 'Download':
     clearControls() 
     clearDisplay () 
     addAudio() 
     addButton( 'download', 'download Audio(', 'Dwnload Audio'), 
     addButton( 'record', 'record ', 'Record Again') 
     break
    default:
      clearControls() 
      clearDisplay() 
      addMessage( 'Your browser does not support mediaDevices')
    break;

}
}
application( stateIndex)