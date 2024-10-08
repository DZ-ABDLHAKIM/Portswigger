---

### What does the [Network Scanning](https://apify.com/dz_omar/network-scanning) do?

The **[Network Scanning](https://apify.com/dz_omar/network-scanning)** is a powerful tool that allows users to scan IP ranges, including AWS and Google Cloud networks, to discover critical information such as services running behind Web Application Firewalls (WAFs), potential vulnerabilities, subdomains, and endpoints. It operates like a Shodan-style search engine but offers deeper insights into small companies' infrastructure that larger search engines might overlook. 

This actor is designed for security professionals, including hackers, bug bounty hunters, and penetration testers, to increase their attack surface and identify vulnerable endpoints across vast networks.

#### Key features:
- **WAF Bypass:** Identify IPs hidden behind WAFs.
- **Fast IP Scanning:** Efficiently scan millions of IP addresses in a short time.
- **Subdomain Discovery:** Reveal new subdomains to extend your attack surface.
- **Vulnerability Detection:** Identify weaknesses in web servers, services, and applications.
- **Endpoint Discovery:** Locate and assess potentially vulnerable endpoints.

### How to Run the [Network Scanning](https://apify.com/dz_omar/network-scanning)

If you're new to [Network Scanning](https://apify.com/dz_omar/network-scanning) or ethical hacking, don't worry. The **[Network Scanning](https://apify.com/dz_omar/network-scanning)** tool is easy to use and highly flexible. You can either use **Masscan** for a fast scan or provide a list of IP addresses to skip Masscan. Here's how:

1. Create a free Apify account using your email.
2. Open the [Network Scanning](https://apify.com/dz_omar/network-scanning) tool in the Apify console.
3. Choose whether to use **Masscan** for scanning by checking or unchecking the **Masscan** option:
   - **If you check the box:** You must provide at least one IP range (in CIDR format).
   - **If you uncheck the box:** You can directly provide a list of individual IP addresses, and the tool will skip the **Masscan** scan.
4. Optionally, you can configure a proxy for the scan, Ensure that you won't be blocked by WAF and access to specific geographical regions.
5. Click the “Start” button to initiate the scan.
6. Analyze the results and download them in structured formats like JSON, XML, CSV, Excel, or HTML for further analysis.

### Input
To start scanning IP ranges or IP addresses, simply fill in the input form. The **[Network Scanning](https://apify.com/dz_omar/network-scanning)** tool recognizes the following input parameters:
> [!NOTE]
> If you are provided more than one IP range, the result won't show up until Masscan is complete from scanning all provided IP ranges.

- **Use Masscan for Scanning (Checkbox)...**: A boolean flag indicating whether or not to use **Masscan** for scanning.
  ![download](https://github.com/user-attachments/assets/1cb2306d-3fca-4c66-8d53-12d07bf18749)
- **CIDR or IP Addresses**: A list of IP ranges in CIDR format or individual IP addresses for scanning.
  - **Using IP ranges (CIDR)**:
        ![download](https://github.com/user-attachments/assets/df0c6412-c011-4225-bbaf-9a4e15cc5c5c)
  - **Using IP Addresses**:
        ![download](https://github.com/user-attachments/assets/b8b1a101-b0c3-44dc-b143-433dee2037f5)

- **Masscan Ports**: (Optional) The port(s) you wish to scan with Masscan The default Port of Masscan is 443 you can add more Port if needed like (e.g., 80, 443 or 0-65535). Required only when Masscan is used.
- **Masscan Rate**: (Optional) The rate limit for **Masscan** (number of packets per second). Required only when Masscan is used.
- **Maximum Results Limit**: (Optional) Set the maximum number of results you want to receive.
- **Proxy Configuration**: (Optional) Use Apify's proxy services to anonymize your scan or access results from a specific geographical location.

### Example Input (Using Masscan):
```json
{
    "Ips_or_CIDR": [
        "3.80.0.0/12",
        "3.208.0.0/12"
    ],
    "Used_Or_Not_Used_Masscan": true,
    "masscan_port": "443",
    "masscan_rate": 10000,
    "max_results": 100,
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": [
            "RESIDENTIAL"
        ],
        "apifyProxyCountry": "BW"
    }
}
```

### Example Input (Skipping Masscan):
```json
{
    "Ips_or_CIDR": [
        "3.91.85.6",
        "3.84.160.117",
        "3.92.19.235"
    ],
    "Used_Or_Not_Used_Masscan": false,
    "max_results": 33,
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": [
            "RESIDENTIAL"
        ],
        "apifyProxyCountry": "BW"
    }
}
```

### Additional Notes:
- You can choose how many results you want by adjusting the `max_results` parameter.
- The **proxyConfiguration** feature allows you to run the scan using Apify's proxy services, ensuring anonymity or access to specific regions.

---

#### Output
You get the output from [Network Scanning](https://apify.com/dz_omar/network-scanning) Data Extractor stored in a tab. Here's an example of some of the output after the scan is complete :

- **In this example I provided this input**:
```json
{
  "Ips_or_CIDR": [
    "3.80.0.0/12"
  ],
  "Used_Or_Not_Used_Masscan": true,
  "masscan_port": "443",
  "masscan_rate": 10000,
  "max_results": 2000,
  "proxyConfiguration": {
    "useApifyProxy": false
  }
}
```
- **The output of this input**:
```json
[
  {
    "title": "",
    "redirected_url": "",
    "request": "https://3.94.15.209:443",
    "port": "443",
    "ip": "3.94.15.209",
    "domain": "*.execute-api.us-east-1.amazonaws.com",
    "response_text": "{\"message\":\"Forbidden\"}",
    "response_headers": {
      "Date": "Mon, 07 Oct 2024 23:21:14 GMT",
      "Content-Type": "application/json",
      "Content-Length": "23",
      "Connection": "keep-alive",
      "x-amzn-RequestId": "c1f2ff47-007d-481e-9a76-02f2bd2c21bc",
      "x-amzn-ErrorType": "ForbiddenException",
      "x-amz-apigw-id": "fTX0oGxcoAMEawg="
    }
  },
...
]
```
![cf6f6720-2ebe-4ca5-9753-6425b9755a22](https://github.com/user-attachments/assets/a92a365f-a2fc-4c84-9a4d-e55780fd84d6)


#### Who can benefit from using [Network Scanning](https://apify.com/dz_omar/network-scanning)?

-   **Security Assessment:** Perform vulnerability assessments and identify exploitable endpoints.
-   **Bug Bounties:** Increase your chances of finding vulnerabilities in bug bounty programs.
-   **Red/Blue Teaming:** Simulate attacks or fortify network defenses by identifying potential entry points.
-   **Penetration Testing:** Discover hidden servers and services for penetration testing.

#### Integrations with the [Network Scanning](https://apify.com/dz_omar/network-scanning)

The [Network Scanning](https://apify.com/dz_omar/network-scanning) integrates seamlessly with Apify’s platform and other tools such as:

-   **Slack**
-   **Zapier**
-   **Google Drive**
-   **GitHub**

You can also use **webhooks** to trigger alerts or actions whenever a scan completes.

---

### FAQ

-   **How much does the [Network Scanning](https://apify.com/dz_omar/network-scanning) cost?**
    The pricing is based on the number of results obtained. For instance, scanning 2,000 IPs costs approximately $0.33, which includes computing units, dataset writes, and external data transfer. You can estimate that scanning 1,000 IPs would cost around $0.165. Apify provides $5 worth of credits for free on their basic plan, which allows you to scan up to 30,303 IPs per month.
-   **Is it legal to scan IPs with the [Network Scanning](https://apify.com/dz_omar/network-scanning)?**
    Yes, as long as you comply with relevant legal guidelines, such as obtaining permission to scan certain IP ranges, especially for companies or cloud providers.

## Support

For issues and support, please create a ticket or contact [fridaytechnolog@gmail.com](mailto:fridaytechnolog@gmail.com).
