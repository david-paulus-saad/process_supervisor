# process_supervisor

## Deployment

To deploy the application using Terraform, follow these steps:

1. Install Terraform. You can download it from the [official website](https://www.terraform.io/downloads.html) and follow the instructions for your operating system.

2. Initialize the Terraform configuration. Navigate to the directory containing the `main.tf` file and run the following command:

   ```
   terraform init
   ```

3. Apply the configuration. Run the following command:

   ```
   terraform apply
   ```

This will create the necessary AWS resources and deploy the application to AWS Lambda.