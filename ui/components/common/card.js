import React from 'react';
import styles from "@/styles/Card.module.css";

const Card = ({ title, description, handleClick }) => {
  return (
    <div className={styles.card}>
      <div className={styles.card_content}>
        <h2 className={styles.card_title}>{title}</h2>
        <p className={styles.card_description}>{description}</p>
        <button className={styles.card_button} onClick={handleClick}>Create Sandbox</button>
      </div>
    </div>
  );
};

export default Card;
