// import { useContext } from "react";
import React from "react";
import Card from "./ui/Card";
// import classes from "./MeetupItem.module.css";
// import FavoritesContext from "../../store/favorites-context";

function Item(props) {
//   const favoriteCtx = useContext(FavoritesContext);
//   const itemIsFavorite = favoriteCtx.itemIsFavorite(props.id);

//   function toggleFavoriteStatusHandler() {
//     if (itemIsFavorite) {
//       favoriteCtx.removeFavorite(props.id);
//     } else {
//       favoriteCtx.addFavorite({
//         id: props.id,
//         title: props.title,
//         descriptions: props.description,
//         image: props.image,
//         adress: props.adress,
//       });
//     }
//   }

  return (
    <Card>
      <li>
        <div>
          <h3>{props.name}</h3>
          <p>{props.description}</p>
          <p>{props.key_1}</p>
        </div>
        {/* <div className={classes.actions}>
          <button onClick={toggleFavoriteStatusHandler}>{itemIsFavorite ? 'Remove from favorites' : 'Add to favorites'}</button>
        </div> */}
      </li>
    </Card>
  );
}

export default Item;
