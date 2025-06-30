import React from 'react';
import { InboxOutlined } from '@ant-design/icons';
import { message, Upload, Input, Button, Select } from 'antd';
const { Dragger } = Upload;
import { useState, useEffect } from 'react';


function UploadBox(){
  const [inputValue, setInputValue] = useState()
  const [conversionType, setConversionType] = useState()
  const props = {

    name: 'file',
    multiple: true,
    action: 'http://127.0.0.1:8080/uploadFileToMP3',
    headers: {},
    data: () => ({
      'conversionDST': inputValue,
      'conversionType': conversionType
    }),
    // onChange(info) {
    //   const { status } = info.file;
    //   if (status !== 'uploading') {
    //     console.log(info.file, info.fileList);
    //   }
    //   if (status === 'done') {
    //     message.success(`${info.file.name} file uploaded successfully.`);
    //   } else if (status === 'error') {
    //     message.error(`${info.file.name} file upload failed.`);
    //   }
    // },
    onDrop(e) {
      console.log('Dropped files', e.dataTransfer.files);
    },
  };

  const handleChange = value => {
    console.log(`selected ${value}`);
  };

  return (
    <div>
      <Select
        defaultValue="MP3"
        style={{ width: 120 }}
        onChange={(value) => setConversionType(value)}
        options={[
          { value: 'mp3', label: 'MP3' },
          { value: 'wav-16bit', label: 'WAV-16bit' },
          { value: 'wav-32bit', label: 'WAV-32bit' },
        ]}
        />

      <Input 
      style={{width: 600}}
      placeholder='Enter destingation path here' 
      onChange={(e)=> setInputValue(e.target.value)}
      
      />

      <div className='mx-auto mt-[20px]'>
        <Dragger {...props}>
          <p className="ant-upload-drag-icon">
            <InboxOutlined />
          </p>
          <p className="ant-upload-text">Click or drag file to this area to upload</p>
          <p className="ant-upload-hint">
            Support for a single or bulk upload. Strictly prohibited from uploading company data or other
            banned files. 
          </p>
        </Dragger>       
      </div>

    </div>
  )
};
export default UploadBox;


