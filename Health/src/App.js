import { useState } from 'react';
import './App.css';
import CalorieTracker from './components/CalorieTracker';
import Excrise from './components/Excrise';
import ChatBot from './components/ChatBot';



function App() {
  const [calorie,setCalorie] = useState(true)
  const [excerise,setExcerise] = useState(false)
  const [chat,setChat] = useState(false)
  const handleClick = ()=> {
    setCalorie(!calorie)
    setExcerise(!excerise)
  }
  const handleChat = () => {
    setChat(!chat)
  }
  return (
    
    <>
    <button className='button set' onClick={handleClick}>{calorie  ? "calorie tacker":"fintness tracker"}</button>
    <button className="button chat" onClick={handleChat}>{!chat ? "ChatBot" :"Close" }</button>
    {calorie && !chat &&  <CalorieTracker /> }
    {excerise &&  !chat && <Excrise />}
    {chat && <ChatBot />}
    </>
  
 
  )
} 

export default App;
