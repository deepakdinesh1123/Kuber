import React from "react";
import styles from "@/styles/Card.module.css";

const Card = ({ title, handleClick, buttonText }) => {
  return (
    <div className={styles.card}>
      <div className={styles.card_content}>
        <h2 className={styles.card_title}>{title}</h2>
        <button className={styles.card_button} onClick={handleClick}>
          {buttonText}
        </button>
      </div>
    </div>
  );
};

export default Card;
