workspace {
    model {
        u = person "User"
        s = softwareSystem "Recipes System" {
            app = container "Recipes Application" "" "Python serverless computing"
            database = container "Recipes Database" "" "Key-value database"
            site = container "Recipes Site" "" "Static website hosting"
        }

        live = deploymentEnvironment "Live" {
            deploymentNode "Amazon Web Services" {
                tags "Amazon Web Services - Cloud"

                deploymentNode "US-East-1" {
                    tags "Amazon Web Services - Region"

                    route53 = infrastructureNode "Route 53" {
                        tags "Amazon Web Services - Route 53"
                    }

                    cloudfront = infrastructureNode "CloudFront" {
                        tags "Amazon Web Services - CloudFront"
                    }

                    apigateway = infrastructureNode "API Gateway" {
                        tags "Amazon Web Services - API Gateway"
                    }

                    lambda = deploymentNode "Lambda" {
                        tags "Amazon Web Services - Lambda"
                        containerInstance app
                    }

                    s3 = deploymentNode "S3" {
                        tags "Amazon Web Services - Simple Storage Service S3 Bucket"
                        containerInstance site
                    }

                    dynamodb = deploymentNode "DynamoDB" {
                        tags "Amazon Web Services - DynamoDB"
                        containerInstance database
                    }
                }
            }

            route53 -> cloudfront "Forwards requests to" "HTTPS"
            route53 -> apigateway "Forwards requests to" "HTTPS"
            cloudfront -> s3 "Forwards requests to" "HTTPS"
            apigateway -> lambda "Forwards requests to" "HTTPS"
            lambda -> dynamodb "Reads from and writes to"
        }
    }

    views {
        deployment s live {
            include *
            autoLayout lr
        }
        theme https://static.structurizr.com/themes/amazon-web-services-2020.04.30/theme.json
    }
}
