import React, { useState, useEffect } from "react";
import { Form } from "@rjsf/mui";
import validator from "@rjsf/validator-ajv8";
import { AxiosRequest, AxiosResponse } from "@/utils/service/api";
import {
  handleCreateInterview,
  handleGetForm,
} from "@/utils/service/interview";

export default function CreateInterview() {
  const [schema, setSchema] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const request: AxiosRequest = {
          type: "GET",
          url: "/interviews/forms",
        };

        const response: AxiosResponse = await handleGetForm(request);

        if (response.success && response.data) {
          setSchema(response.data);
        } else {
          console.error("Invalid schema data received");
        }
      } catch (error) {
        console.error("Error fetching schema data:", error);
      }
    };

    fetchData();
  }, []);

  const onSubmit = async ({ formData }, e) => {
    try {
      const postRequest: AxiosRequest = {
        type: "POST",
        url: "/interviews/interview",
        data: formData,
      };

      const response: AxiosResponse = await handleCreateInterview(postRequest);

      if (response.success) {
        console.log("Data submitted successfully");
        window.alert("Interview created successfully");
      } else {
        console.error("API request failed");
        window.alert("Interview creation failed");
      }
    } catch (error) {
      console.error("API request error:", error);
    }
  };

  const uiSchema = {
    config: {
      "ui:widget": "textarea",
    },
  };

  return (
    <div className="form-container">
      {schema && (
        <Form
          schema={schema}
          validator={validator}
          onSubmit={onSubmit}
          uiSchema={uiSchema}
        />
      )}
    </div>
  );
}
