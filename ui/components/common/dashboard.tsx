import React from "react";
import Card from "./card";
import styles from "../../styles/Dashboard.module.css";

interface DashboardProps {
  title: string;
  cardData: Array<{
    id: string;
    type: string;
    title: string;
  }>;
  onCreateClick: () => void;
  onDeleteClick: (id: string, type: string) => void;
  onEditClick: (id: string, type: string) => void;
}

const Dashboard: React.FC<DashboardProps> = ({
  title,
  cardData,
  onCreateClick,
  onDeleteClick,
  onEditClick,
}) => {
  return (
    <div className={styles.dashboard}>
      <div className={styles.header}>
        <h1 className={styles.dashboardTitle}>{title}</h1>
        <button className={styles.createButton} onClick={onCreateClick}>
          Create
        </button>
      </div>
      <hr className={styles.dashboardLine} />
      <div className={styles.contentContainer}>
        <div className={styles.cardContainer}>
          {cardData.map((data, index) => (
            <Card
              key={index}
              id={data.id}
              type={data.type}
              title={data.title}
              onEditClick={onEditClick}
              onDeleteClick={onDeleteClick}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
