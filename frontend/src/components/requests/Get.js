import React, { useState, useEffect } from "react";

function GetData(props) {
  const [data, setData] = useState([{}]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    fetch(props.path)
      .then((response) => {
        return response.json();
      })
      .then((raw_data) => {
        // Work with JSON data here
        setData(raw_data.members);
      })
      .catch((err) => {
        // Do something for an error here
        console.log("Error Reading data " + err);
      });
    setLoading(false);
  }, []);

  if (isLoading) {
    return <p>Loading</p>
  } else {
      props.children
    return data
  }
}

export default GetData;
