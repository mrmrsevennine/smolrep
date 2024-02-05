Shared Dependencies:

1. **HTML Elements ID Names**: 
   - `navbar` for the navigation bar.
   - `main-content` for the main content of each page.
   - `footer` for the footer of each page.
   - `service-list` for the list of services on the services page.
   - `book-form` for the booking form on the book page.
   - `insurance-info` for the insurance information on the insurance page.
   - `warranty-info` for the warranty information on the warranty page.

2. **CSS Classes**:
   - `navbar-style` for styling the navigation bar.
   - `main-content-style` for styling the main content of each page.
   - `footer-style` for styling the footer of each page.
   - `service-list-style` for styling the list of services on the services page.
   - `book-form-style` for styling the booking form on the book page.
   - `insurance-info-style` for styling the insurance information on the insurance page.
   - `warranty-info-style` for styling the warranty information on the warranty page.

3. **JavaScript Functions**:
   - `loadServices()` to load the list of services on the services page.
   - `bookService()` to handle the booking of services on the book page.
   - `loadInsuranceInfo()` to load the insurance information on the insurance page.
   - `loadWarrantyInfo()` to load the warranty information on the warranty page.

4. **Data Schemas**:
   - `Service` schema for the services data, which includes fields like `name`, `description`, `price`.
   - `Booking` schema for the booking data, which includes fields like `serviceId`, `customerName`, `customerEmail`, `date`.
   - `Insurance` schema for the insurance data, which includes fields like `name`, `description`, `price`.
   - `Warranty` schema for the warranty data, which includes fields like `name`, `description`, `price`.

5. **Message Names**:
   - `SERVICE_LOADED` message when the services data is loaded.
   - `BOOKING_SUBMITTED` message when a booking is submitted.
   - `INSURANCE_LOADED` message when the insurance data is loaded.
   - `WARRANTY_LOADED` message when the warranty data is loaded.

6. **External Libraries**:
   - Tailwind CSS for styling.