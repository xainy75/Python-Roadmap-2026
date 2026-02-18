"""
Example: Data Processing with Good Naming Conventions
Demonstrates proper naming in a data processing context.
"""

from typing import List, Dict, Any
import json


# Constants for configuration
DEFAULT_BATCH_SIZE = 100
MAX_RETRY_ATTEMPTS = 3
ERROR_THRESHOLD = 0.1


class DataValidator:
    """Validates data according to defined rules."""
    
    def __init__(self):
        self.validation_errors = []
    
    def is_valid_record(self, record: Dict[str, Any]) -> bool:
        """
        Check if a data record is valid.
        
        Args:
            record: Dictionary containing record data
            
        Returns:
            True if record is valid, False otherwise
        """
        required_fields = ["id", "name", "value"]
        
        for field_name in required_fields:
            if field_name not in record:
                error_message = f"Missing required field: {field_name}"
                self.validation_errors.append(error_message)
                return False
        
        return True
    
    def get_validation_errors(self) -> List[str]:
        """Retrieve all validation errors."""
        return self.validation_errors
    
    def clear_errors(self):
        """Clear all stored validation errors."""
        self.validation_errors = []


class DataProcessor:
    """Processes and transforms data records."""
    
    def __init__(self):
        self.validator = DataValidator()
        self.processed_count = 0
        self.failed_count = 0
    
    def process_records(self, raw_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Process a list of raw data records.
        
        Args:
            raw_records: List of dictionaries containing raw data
            
        Returns:
            List of processed and validated records
        """
        processed_records = []
        
        for record_index, raw_record in enumerate(raw_records):
            try:
                if self.validator.is_valid_record(raw_record):
                    processed_record = self._transform_record(raw_record)
                    processed_records.append(processed_record)
                    self.processed_count += 1
                else:
                    print(f"Invalid record at index {record_index}")
                    self.failed_count += 1
            except Exception as processing_error:
                print(f"Error processing record {record_index}: {processing_error}")
                self.failed_count += 1
        
        return processed_records
    
    def _transform_record(self, raw_record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform a raw record into processed format.
        
        Args:
            raw_record: Dictionary containing raw data
            
        Returns:
            Transformed record dictionary
        """
        processed_record = {
            "record_id": raw_record["id"],
            "display_name": raw_record["name"].upper(),
            "numeric_value": float(raw_record["value"]),
            "is_processed": True
        }
        return processed_record
    
    def calculate_success_rate(self) -> float:
        """
        Calculate the percentage of successfully processed records.
        
        Returns:
            Success rate as a percentage (0.0 to 100.0)
        """
        total_records = self.processed_count + self.failed_count
        
        if total_records == 0:
            return 0.0
        
        success_rate = (self.processed_count / total_records) * 100
        return success_rate
    
    def get_processing_summary(self) -> Dict[str, Any]:
        """
        Get a summary of processing statistics.
        
        Returns:
            Dictionary containing processing metrics
        """
        summary = {
            "total_processed": self.processed_count,
            "total_failed": self.failed_count,
            "success_rate_percent": self.calculate_success_rate()
        }
        return summary


class FileHandler:
    """Handles file operations for data processing."""
    
    def read_json_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Read data from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            List of records from the file
        """
        try:
            with open(file_path, 'r') as input_file:
                records = json.load(input_file)
                print(f"Successfully loaded {len(records)} records from {file_path}")
                return records
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return []
        except json.JSONDecodeError as json_error:
            print(f"Invalid JSON in file: {json_error}")
            return []
    
    def write_json_file(self, file_path: str, data: List[Dict[str, Any]]) -> bool:
        """
        Write data to a JSON file.
        
        Args:
            file_path: Path where the file should be written
            data: List of records to write
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(file_path, 'w') as output_file:
                json.dump(data, output_file, indent=2)
                print(f"Successfully wrote {len(data)} records to {file_path}")
                return True
        except IOError as io_error:
            print(f"Error writing file: {io_error}")
            return False


def filter_records_by_threshold(records: List[Dict[str, Any]], 
                                 threshold_value: float) -> List[Dict[str, Any]]:
    """
    Filter records based on a numeric threshold.
    
    Args:
        records: List of record dictionaries
        threshold_value: Minimum value to include
        
    Returns:
        Filtered list of records
    """
    filtered_records = [
        record for record in records 
        if record.get("numeric_value", 0) >= threshold_value
    ]
    return filtered_records


def calculate_average_value(records: List[Dict[str, Any]]) -> float:
    """
    Calculate the average numeric value across all records.
    
    Args:
        records: List of record dictionaries
        
    Returns:
        Average value, or 0.0 if no records
    """
    if not records:
        return 0.0
    
    total_value = sum(record.get("numeric_value", 0) for record in records)
    average_value = total_value / len(records)
    return average_value


# Example usage
if __name__ == "__main__":
    # Sample data
    sample_records = [
        {"id": 1, "name": "Alice", "value": 100},
        {"id": 2, "name": "Bob", "value": 200},
        {"id": 3, "name": "Charlie", "value": 150},
        {"id": 4, "name": "Invalid"},  # Missing 'value' field
        {"id": 5, "name": "Diana", "value": 300}
    ]
    
    print("=== Data Processing Example ===\n")
    
    # Process the records
    data_processor = DataProcessor()
    processed_records = data_processor.process_records(sample_records)
    
    # Display results
    print(f"\nProcessed Records:")
    for record in processed_records:
        print(f"  {record}")
    
    # Show processing summary
    processing_summary = data_processor.get_processing_summary()
    print(f"\nProcessing Summary:")
    print(f"  Successfully processed: {processing_summary['total_processed']}")
    print(f"  Failed: {processing_summary['total_failed']}")
    print(f"  Success rate: {processing_summary['success_rate_percent']:.1f}%")
    
    # Filter records
    minimum_threshold = 150
    high_value_records = filter_records_by_threshold(processed_records, minimum_threshold)
    print(f"\nRecords with value >= {minimum_threshold}: {len(high_value_records)}")
    
    # Calculate average
    average_value = calculate_average_value(processed_records)
    print(f"Average value: {average_value:.2f}")
