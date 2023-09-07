import React, { useState, useEffect } from "react";
import IDE from "@/components/ide/ide";
import styles from "../../styles/Interview.module.css";

function Interview() {
  const [showProblemStatement, setShowProblemStatement] = useState(false);
  const initialTimerValue = 10;
  const [timer, setTimer] = useState(initialTimerValue); // Initial timer value in seconds

  const toggleProblemStatement = () => {
    setShowProblemStatement(!showProblemStatement);
  };

  const handleSubmit = () => {
    // Log the submit action
    console.log("Submit button clicked");
  };

  const handleTest = () => {
    // Log the test action
    console.log("Test button clicked");
  };

  useEffect(() => {
    let timerInterval;

    if (timer > 0) {
      timerInterval = setInterval(() => {
        setTimer((prevTimer) => {
          if (prevTimer <= 1) {
            clearInterval(timerInterval);
            // Timer has reached 0, trigger submit
            handleSubmit();
            return 0;
          }
          return prevTimer - 1;
        });
      }, 1000);
    }

    return () => clearInterval(timerInterval);
  }, [timer]);

  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds < 10 ? "0" : ""}${remainingSeconds}`;
  };

  return (
    <div className={styles["interview-container"]}>
      <div className={styles["top-right"]}>
        <span className={styles["timer-display"]}>
          Timer: {formatTime(timer)} {/* Display formatted time */}
        </span>
        <button onClick={handleSubmit}>Submit</button>
        <button onClick={handleTest}>Test</button>
        <button onClick={toggleProblemStatement}>Problem Statement</button>
      </div>
      <IDE />
      {showProblemStatement && (
        <div className={styles["modal-overlay"]}>
          <div className={styles["modal"]}>
            <button
              onClick={toggleProblemStatement}
              className={styles["close-button"]}
            >
              Close
            </button>
            <div className={styles["modal-content"]}>
              <h2>Problem Statement</h2>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default Interview;
