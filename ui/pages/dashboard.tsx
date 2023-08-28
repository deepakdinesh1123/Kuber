import styles from "styles/Dashboard.module.css";
import { useRouter } from "next/router";
import { useEffect } from "react";
import { getCookie } from "cookies-next";

const Dashboard = () => {
  const router = useRouter();
  useEffect(() => {
    if (!getCookie("access_token")) {
      router.push("/");
    }
  });

  return (
    <div className={styles.container}>
      <div className={styles.buttonsContainer}>
        <button
          className={styles.button}
          onClick={() => {
            router.push("/interviews/create");
          }}
        >
          New Interview
        </button>
        <button
          className={styles.button}
          onClick={() => {
            router.push("/images/create");
          }}
        >
          New Image
        </button>
        <button
          className={styles.button}
          onClick={() => {
            router.push("/environments/create");
          }}
        >
          New Environment
        </button>
      </div>
    </div>
  );
};

export default Dashboard;
