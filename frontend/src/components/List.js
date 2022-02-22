import React from "react";
import Item from "./Item";

function List(props) {
  return props.elements.map((element, i) => (
    <Item key={i} key_1={element.key} name={element.username} description={element.password}/>
    ));
}

export default List;
