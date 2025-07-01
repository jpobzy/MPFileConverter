import Versions from './components/Versions'
import electronLogo from './assets/electron.svg'
import { Button, DatePicker } from 'antd';
import React from 'react';
import UploadBox from './components/UploadBox';


function App() {
  const ipcHandle = () => window.electron.ipcRenderer.send('ping')

  return (
    <>
      <UploadBox/>
    </>
  )
}

export default App
