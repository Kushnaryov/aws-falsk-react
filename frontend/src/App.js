import "./App.css";
import React, { useState, useEffect } from "react";
import List from "./components/List";
import axios from 'axios';
const axios_ = axios.create({
  baseURL: 'http://localhost:5000',
  // baseURL: '/backend',
  headers: { 'Content-Type': 'application/json' },
})

function App() {
  const [loadedData, setLoadedData] = useState([{}]);
  const [isLoading, setLoading] = useState(true);
  useEffect(() => {
    setLoading(true);
    axios_.get('/send')
      .then((response) => {
        // Work with JSON data here
        const data = [];
        console.log(response.data)
        for (const key in response.data) {
          console.log(key)
          const element = {
            key: key,
            
            ...response.data[key],
          };
          data.push(element);
        }
        console.log(data)
        setLoading(false);
        setLoadedData(data);
      })
  }, []);

  if (isLoading) {
    return <p>Loading</p>;
  } else {
    return <div><List elements={loadedData} /></div>;
  }
}


export default App;
