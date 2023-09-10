import React, { useState, useEffect } from "react";
import { useRouter } from "next/router";
import { Form } from "@rjsf/mui";
import validator from "@rjsf/validator-ajv8";
import { AxiosRequest, AxiosResponse } from "@/utils/service/api";
import {
  handleCreateEnvironment,
  handleGetForm,
} from "@/utils/service/environment";

export default function CreateEnvironment() {
  const router = useRouter();
  const [schema, setSchema] = useState(null);
  const { formId } = router.query;

  useEffect(() => {
    const fetchData = async () => {
      try {
        let requestUrl = "/environments/forms";

        if (formId) {
          requestUrl = `/environments/form/${formId}`;
        }

        const request: AxiosRequest = {
          type: "GET",
          url: requestUrl,
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
  }, [formId]);

  const onSubmit = async ({ formData }, e) => {
    try {
      const postRequest: AxiosRequest = {
        type: "POST",
        url: "/environments/environment",
        data: formData,
      };

      const response: AxiosResponse = await handleCreateEnvironment(
        postRequest,
      );

      if (response.success) {
        console.log("Data submitted successfully");
        window.alert("Environment created successfully");
        router.push("/dashboard");
      } else {
        console.error("API request failed");
        window.alert("Environment creation failed");
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
