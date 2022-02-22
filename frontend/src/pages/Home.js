import React from "react";
import { useState, useEffect } from "react";

import MeetupList from "../components/meetups/MeetupList";

const url_to_fech = '/members'
//const url_to_fech = "https://react-app-18ecb-default-rtdb.europe-west1.firebasedatabase.app/meetups.json"

function HomePage() {
  const [isLoading, setIsLoading] = useState(true)
  const [loadedMeetups, setLoadedMeetups] = useState([])

  useEffect(() => {
    setIsLoading(true)
    fetch(url_to_fech
      
    ).then(response => {
      return response.json();
    }).then(data => {
      const meetups = [];

      for (const key in data) {
        const meetup = {
          id: key,
          ...data[key]
        }
        meetups.push(meetup)
      }
      setIsLoading(false)
      setLoadedMeetups(meetups)
    });
  }, [])

  

  if (isLoading) {
    return <section>
      <p>...Loading</p>
    </section>
  } 

  return (
    <section>
        
    </section>
  );
}

export default HomePage;
