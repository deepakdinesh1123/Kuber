import styles from "styles/Dashboard.module.css";
import Dashboard from "@/components/common/dashboard";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { getCookie } from "cookies-next";
import {
  fetchEnvironmentData,
  fetchInterviewData,
  fetchSandboxData,
} from "@/utils/api_method_handler/dataFetch";
import {
  delEnvironment,
  delInterview,
} from "@/utils/api_method_handler/delHandler";

const MainDashboard = () => {
  const [environmentData, setEnvironmentData] = useState([]);
  const [interviewData, setInterviewData] = useState([]);
  const [sandboxData, setSandboxData] = useState([]);
  const router = useRouter();

  const createEnv = () => {
    router.push("/environments/create");
  };

  const createInterview = () => {
    router.push("/interviews/create");
  };

  const createImage = () => {
    console.log("Create image button clicked");
  };

  const createSandbox = () => {
    console.log("Create sandbox button clicked");
  };

  const editCard = (id, type) => {
    console.log(id, type);
    const editUrl = `/${type}/create?formId=${id}`;
    router.push(editUrl);
    // router.push("/interviews/create")
  };

  const deleteCard = async (id, type) => {
    try {
      const shouldDelete = window.confirm(
        `Are you sure you want to delete this ${type}`,
      );

      if (!shouldDelete) {
        console.log("Deletion canceled.");
        return;
      }
      if (type === "environments") {
        const response = await delEnvironment(id);
        if (response.success) {
          console.log(`Deleted environment with ID ${id}`);
          setEnvironmentData((prevData) =>
            prevData.filter((env) => env.id !== id),
          );
        } else {
          console.error("Error deleting environment:");
        }
      } else if (type === "interviews") {
        const response = await delInterview(id);
        if (response.success) {
          console.log(`Deleted interview with ID ${id}`);
          setInterviewData((prevData) =>
            prevData.filter((interview) => interview.id !== id),
          );
        } else {
          console.error("Error deleting Interview:");
        }
      } else if (type === "sandboxs") {
        console.log("No method yet :)");
        // const response = await delInterview(id);
        // if (response.success) {
        //   console.log(`Deleted sandbox with ID ${id}`);
        //   setSandboxData((prevData) => prevData.filter((sandbox) => sandbox.id !== id));
        // } else {
        //   console.error('Error deleting sandbox:');
        // }
      }
    } catch (error) {
      console.error("Error deleting card:", error);
    }
  };

  const fetchData = async () => {
    if (!getCookie("access_token")) {
      router.push("/");
      return;
    }

    try {
      const environmentResponse = await fetchEnvironmentData();
      const interviewResponse = await fetchInterviewData();
      const sandboxResponse = await fetchSandboxData();

      if (environmentResponse.success) {
        setEnvironmentData(
          environmentResponse.data.map((environment) => ({
            title: environment.env_name,
            id: environment.env_id,
            type: "environments",
          })),
        );
      } else {
        console.error("Invalid environment data received");
      }

      if (interviewResponse.success) {
        setInterviewData(
          interviewResponse.data.map((interview) => ({
            title: interview.name,
            id: interview.interview_id,
            type: "interviews",
          })),
        );
      } else {
        console.error("Invalid interview data received");
      }

      if (sandboxResponse.success) {
        setSandboxData(
          sandboxResponse.data.map((sandbox) => ({
            title: sandbox.name,
            id: sandbox.id,
            type: "sandboxs",
          })),
        );
      } else {
        console.error("Invalid interview data received");
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const cardData = [{ title: "Card 1 Title" }];

  return (
    <div className={styles.container}>
      <div className="App">
        <Dashboard
          title="Images"
          cardData={cardData}
          onCreateClick={createImage}
          onDeleteClick={deleteCard}
        />
      </div>
      <div className="App">
        <Dashboard
          title="Environments"
          cardData={environmentData}
          onCreateClick={createEnv}
          onDeleteClick={deleteCard}
          onEditClick={editCard}
        />
      </div>
      <div className="App">
        <Dashboard
          title="Sandboxes"
          cardData={sandboxData}
          onCreateClick={createSandbox}
          onDeleteClick={deleteCard}
        />
      </div>
      <div className="App">
        <Dashboard
          title="Interviews"
          cardData={interviewData}
          onCreateClick={createInterview}
          onDeleteClick={deleteCard}
          onEditClick={editCard}
        />
      </div>
    </div>
  );
};

export default MainDashboard;
