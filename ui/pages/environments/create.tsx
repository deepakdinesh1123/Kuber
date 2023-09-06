import React, { useState } from 'react';
import { Form } from '@rjsf/mui';
import { RJSFSchema } from '@rjsf/utils'
import validator from '@rjsf/validator-ajv8';

export default function CreateEnvironment() {
  // const [formData, setFormData] = useState({});
  const schema: RJSFSchema = {
    "type": "object",
    "required": [
        "env_name",
        "image",
        "config",
        "type"
    ],
    "properties": {
        "env_name": {
            "title": "Env name",
            "type": "string"
        },
        "image": {
            "title": "Image",
            "type": "string",
            "enumNames": [
                "img_1"
            ],
            "enum": [
                "a83ebbf2-251f-49de-a492-917e3d726769"
            ]
        },
        "config": {
            "title": "Config",
            "type": "string"
        },
        "type": {
            "title": "Type",
            "type": "string",
            "enumNames": [
                "docker-compose",
                "docker"
            ],
            "enum": [
                "compose",
                "docker"
            ]
        },
        "private": {
            "title": "Private",
            "type": "boolean",
            "oneOf": [
                {
                    "title": "Enable",
                    "const": true
                },
                {
                    "title": "Disable",
                    "const": false
                }
            ]
        }
    }
}

// function handleformsubmit() {
//   // setFormData(formData);
//   console.log('Form data submitted:', FormData);
    
// }
const onSubmit = ({formData}, e) => console.log("Data submitted: ",  formData);

  return (
   <div className="form-container">
      <Form 
      schema={schema} 
      validator={validator}
      onSubmit={onSubmit}/>
   </div>
  );
}