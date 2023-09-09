import React from "react";
import styles from "../.././styles/Card.module.css";

interface CardProps {
  title: string;
  id: string;
  type: string;
  onEditClick: () => void;
  onDeleteClick: (id: string, type: string) => void;
}

const Card: React.FC<CardProps> = ({
  title,
  id,
  type,
  onEditClick,
  onDeleteClick,
}) => {
  return (
    <div className={styles.card}>
      <h2 className={styles["card-title"]}>{title}</h2>
      <div className={styles["card-buttons"]}>
        <button className={styles["edit-button"]} onClick={onEditClick}>
          Edit
        </button>
        <button
          className={styles["delete-button"]}
          onClick={() => onDeleteClick(id, type)}
        >
          Delete
        </button>
      </div>
    </div>
  );
};

export default Card;
