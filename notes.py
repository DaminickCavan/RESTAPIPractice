'''
REST stands for Representational State Transfer
it's a pattern for client and server communications over a network
provides a set of constraints for software architecture for performance, scalability, simplicity and reliability

- it's stateless, meaning the server wont maintain any state between requests from the client
- client and server must be decoupled from each other, allowing each to develop seperately
- it's cacheable, the data retrieved from the server should be cached by the client or server
- the server will demand a uniform interface for accessing resources without defining their representation
- the client may access resouces indirecty through a layered system such as a proxy or load balancer
- you can code on demmand. Ther server may transfer code to the client that it can run via JavaScript for example on a single-page application
- PUT fully updates an existing source
- PATCH Partially updates an existing source


'''